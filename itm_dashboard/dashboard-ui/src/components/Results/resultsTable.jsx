import React from 'react';
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import TableContainer from "@material-ui/core/TableContainer";
import AlignmentScoreBox from './alignmentScore';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';

import { Query } from 'react-apollo';
import gql from 'graphql-tag';

const getScenarioNamesQueryName = "getScenarioNames";
const getPerformerADMByScenarioName = "getPerformerADMsForScenario";
const getTestByADMandScenarioName = "getTestByADMandScenario";

const scenario_names_aggregation = gql`
    query getScenarioNames{
        getScenarioNames
    }`;
const performer_adm_by_scenario = gql`
    query getPerformerADMsForScenario($scenarioID: ID){
        getPerformerADMsForScenario(scenarioID: $scenarioID)
    }`;
const test_by_adm_and_scenario = gql`
    query getTestByADMandScenario($scenarioID: ID, $admName: ID){
        getTestByADMandScenario(scenarioID: $scenarioID, admName: $admName)
    }`;

class ResultsTable extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            adm: "",
            scenario: "",
        }
    }

    setScenario(target){
        this.setState({
            scenario: target
        });
    }

    setPerformerADM(target){
        this.setState({
            adm: target
        });
    }

    formatScenarioString(id) {
        if(id.indexOf("ADEPT1") > -1 ) {
            return ("BBN: " + id);
        } else {
            return ("Soartech: " + id);
        }
    }

    formatADMString(peformerADMString) {
        if(peformerADMString.indexOf("ALIGN-ADM") > -1 ) {
            return ("Kitware: " + peformerADMString);
        } else if (peformerADMString.indexOf("TAD") > -1){
            return ("Parallax: " + peformerADMString);
        } else {
            return peformerADMString;
        }
    }

    snakeCaseToNormalCase(string) {
        return string
            .replace(/_/g, ' ')
            .replace(/(^\w|\s\w)/g, m => m.toUpperCase());
    }

    isObject(item) {
        return (typeof item === 'object' && !Array.isArray(item) && item !== null);
    }

    renderNestedItems(item) {
        if (this.isObject(item)) {
            return this.renderNestedTable(item);
        } else if (Array.isArray(item)) {
            return (
                <ul>
                    {item.map((el, i) => <li key={i}>{this.renderNestedItems(el)}</li>)}
                </ul>
            );
        } else {
            return <span>{item}</span>;
        }
    }

    renderNestedTable(tableData) {
        return(
            <Table size="small">
                <TableBody>
                    {Object.entries(tableData).map(([key, value], i) => (
                        <TableRow key={i}>
                            <TableCell className="tableCell">
                                <strong>{this.snakeCaseToNormalCase(key)}</strong>
                            </TableCell>
                            <TableCell className="tableCell">{this.renderNestedItems(value)}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        );
    }

    render() {
        return (
            <div className="layout">
                <div className="layout-board">
                    <div className="nav-section">
                        <div className="nav-header">
                            <span className="nav-header-text">Scenario</span>
                        </div>
                        <div className="nav-menu">
                            <Query query={scenario_names_aggregation}>
                            {
                                ({ loading, error, data }) => {
                                    if (loading) return <div>Loading ...</div> 
                                    if (error) return <div>Error</div>

                                    const scenarioNameOptions = data[getScenarioNamesQueryName];
                                    let scenariosArray = [];
                                    for(let i=0; i < scenarioNameOptions.length; i++) {
                                        scenariosArray.push({
                                            "value": scenarioNameOptions[i]._id.id, 
                                            "name": scenarioNameOptions[i]._id.name
                                        });
                                    }
                                    scenariosArray.sort((a, b) => (a.value > b.value) ? 1 : -1);

                                    return (
                                        <List className="nav-list" component="nav" aria-label="secondary mailbox folder">
                                            {scenariosArray.map((item,key) =>
                                                <ListItem className="nav-list-item" id={"scenario_" + key} key={"scenario_" + key}
                                                    button
                                                    selected={this.state.scenario === item.value}
                                                    onClick={() => this.setScenario(item.value)}>
                                                    <ListItemText primary={this.formatScenarioString(item.value)} />
                                                </ListItem>
                                            )}
                                        </List>
                                    )
                                }
                            }
                            </Query>
                        </div>
                        {this.state.scenario !== "" &&
                            <>
                                <div className="nav-header">
                                    <span className="nav-header-text">Performer/ADM</span>
                                </div>
                                <div className="nav-menu">
                                <Query query={performer_adm_by_scenario} variables={{"scenarioID": this.state.scenario}}>
                                    {
                                        ({ loading, error, data }) => {
                                            if (loading) return <div>Loading ...</div> 
                                            if (error) return <div>Error</div>

                                            const performerADMOptions = data[getPerformerADMByScenarioName];
                                            let performerADMArray = [];
                                            for(let i=0; i < performerADMOptions.length; i++) {
                                                performerADMArray.push({
                                                    "value": performerADMOptions[i],
                                                    "name": performerADMOptions[i]
                                                });
                                            }
                                            performerADMArray.sort((a, b) => (a.value > b.value) ? 1 : -1);

                                            return (
                                                <List className="nav-list" component="nav" aria-label="secondary mailbox folder">
                                                    {performerADMArray.map((item,key) =>
                                                        <ListItem className="nav-list-item" id={"performeradm_" + key} key={"performeradm_" + key}
                                                            button
                                                            selected={this.state.adm === item.value}
                                                            onClick={() => this.setPerformerADM(item.value)}>
                                                            <ListItemText primary={this.formatADMString(item.value)} />
                                                        </ListItem>
                                                    )}
                                                </List>
                                            )
                                        }
                                    }
                                    </Query>
                                </div>
                            </>
                        }
                    </div>
                    <div className="test-overview-area">
                        {(this.state.scenario !== "" && this.state.adm !== "") &&
                            <Query query={test_by_adm_and_scenario} variables={{"scenarioID": this.state.scenario, "admName": this.state.adm}}>
                            {
                                ({ loading, error, data }) => {
                                    if (loading) return <div>Loading ...</div> 
                                    if (error) return <div>Error</div>

                                    const testData = data[getTestByADMandScenarioName];

                                    return (
                                        <>
                                            {testData !== null && testData !== undefined &&
                                            <>
                                                <AlignmentScoreBox performer={this.formatADMString(this.state.adm)} data={testData} scenario={this.state.scenario}/>
                                                <div className='paper-container'>
                                                    <TableContainer style={{ maxHeight: '70vh' }}>
                                                        <Table stickyHeader aria-label="simple table">
                                                            <TableHead>
                                                                <TableRow>
                                                                    <TableCell className="tableCell main">Command</TableCell>
                                                                    <TableCell className="tableCell main">Parameters</TableCell>
                                                                    <TableCell className="tableCell main">Response</TableCell>
                                                                    </TableRow>
                                                            </TableHead>
                                                            <TableBody>
                                                                {testData.history.map((item, index) => (
                                                                    <TableRow key={index} className={item.command.startsWith('TA1') ? 'ta1-row' : ''}>
                                                                        <TableCell className="tableCell main">{item.command}</TableCell>
                                                                        <TableCell className="tableCell main">{this.renderNestedItems(item.parameters)}</TableCell>
                                                                        <TableCell className="tableCell main">{this.renderNestedItems(item.response)}</TableCell>
                                                                    </TableRow>
                                                                    ))}
                                                            </TableBody>
                                                        </Table>
                                                    </TableContainer>
                                                </div>
                                            </>
                                            }
                                        </>
                                    )
                                }
                            }
                            </Query>
                        }
                    </div>
                </div>
            </div>
        );
    }
}

export default ResultsTable;
