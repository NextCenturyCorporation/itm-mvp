import React from 'react';
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import TableContainer from "@material-ui/core/TableContainer";
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';

import { Query } from 'react-apollo';
import gql from 'graphql-tag';

const getScenarioName = "getScenario";
const getScenarioNamesQueryName = "getScenarioNames";
const scenario_names_aggregation = gql`
    query getScenarioNames{
        getScenarioNames
    }`;
const GET_ITM_SCENARIO = gql`
    query getScenario($scenarioId: ID) {
        getScenario(scenarioId: $scenarioId) {
            id
            name
            state {
                mission {
                    unstructured
                    mission_type
                }
                environment {
                    unstructured
                    aidDelay
                    weather
                    location
                    visibility
                    noise_ambient
                    noise_peak
                }
                threat_state {
                    unstructured
                    threats
                }
                supplies {
                    type
                    quantity
                }
                casualties {
                    name
                    unstructured
                    injuries {
                        location
                        name
                        severity
                    }
                    mental_status
                    demographics {
                        age
                        sex
                        rank
                    }
                    vitals {
                        hrpmin
                        mm_hg
                        rr
                        sp_o2
                        pain
                    }
                }
            }
        }
    }`;

class ScenarioPage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            scenario: "",
        }
    }

    setScenario(target){
        this.setState({
            scenario: target
        });
    }

    formatScenarioString(id) {
        if(id.indexOf("ADEPT1") > -1 ) {
            return ("BBN: " + id);
        } else {
            return ("Soartech: " + id);
        }
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

    renderNestedTable(data) {
        return(
            <Table size="small">
                <TableBody>
                    {Object.entries(data).map(([key, value], i) => (
                        key !== "__typename" &&
                        <TableRow key={i}>
                            <TableCell className="tableCell">{key}</TableCell>
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
                    </div>
                    <div className="test-overview-area">
                        {(this.state.scenario !== "") &&
                            <Query query={GET_ITM_SCENARIO} variables={{"scenarioId": this.state.scenario}}>
                            {
                                ({ loading, error, data }) => {
                                    if (loading) return <div>Loading ...</div> 
                                    if (error) return <div>Error</div>

                                    const scenarioData = data[getScenarioName];

                                    return (
                                        <>
                                            <TableContainer style={{ maxHeight: '70vh' }}>
                                                <Table stickyHeader aria-label="simple table">
                                                    <TableHead>
                                                        <TableRow>
                                                            <TableCell className="tableCell main">Scenario: {this.formatScenarioString(this.state.scenario)}</TableCell>
                                                        </TableRow>
                                                    </TableHead>
                                                    <TableBody>
                                                        <TableRow style={{ backgroundColor: '#f4f4f4'}}>
                                                            <TableCell className="tableCell main">
                                                                {this.renderNestedItems(scenarioData)}
                                                            </TableCell>
                                                        </TableRow>
                                                    </TableBody>
                                                </Table>
                                            </TableContainer>
                                        </>
                                    )
                                }
                            }
                            </Query>
                        }
                    </div>
                </div>
            </div>
        )
    }
}

export default ScenarioPage;
