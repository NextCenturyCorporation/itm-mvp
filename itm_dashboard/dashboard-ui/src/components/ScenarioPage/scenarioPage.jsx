import React from 'react';
import { useState } from 'react';
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import TableContainer from "@material-ui/core/TableContainer";
import Paper from '@material-ui/core/Paper';
import ScenarioPageModal from './scenarioPageModal';

import { Query } from 'react-apollo';
import gql from 'graphql-tag';

const GET_ALL_ITM_SCENARIOS = gql`
    query getAllScenarios($id: ID) {
        getAllScenarios(id: $id) {
            name
            id
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


const ScenarioPage = () => {
    const isObject = (item) => {
        return (typeof item === 'object' && !Array.isArray(item) && item !== null);
    }

    const renderNestedItems = (item) => {
        if (isObject(item)) {
            return <NestedTable data={item} />
        } else if (Array.isArray(item)) {
            return (
                <ul>
                    {item.map((el, i) => <li key={i}>{renderNestedItems(el)}</li>)}
                </ul>
            );
        } else {
            return <span>{item}</span>;
        }
    }

    const NestedTable = ({ data }) => (
        <Table size="small">
            <TableBody>
                {Object.entries(data).map(([key, value], i) => (
                    key !== "__typename" &&
                    <TableRow key={i}>
                        <TableCell className="tableCell">{key}</TableCell>
                        <TableCell className="tableCell">{renderNestedItems(value)}</TableCell>
                    </TableRow>
                ))}
            </TableBody>
        </Table>
    );
    
    const MainTable = () => {
        const [selectedNames, setSelectedName] = useState([]);
        const [checkedItems, setCheckedItems] = useState([]);

        const handleAddName = (name) => {
            setSelectedName([...selectedNames, name]);
        };

        const handleRemoveName = (name) => {
            setSelectedName(selectedNames.filter((item) => item !== name));
        };
          

        return (
            <Query query={GET_ALL_ITM_SCENARIOS} variables={{ "id": "Testing_12345" }}>
                {
                    ({ loading, error, data }) => {
                        if (loading) return <div>Loading ...</div> 
                        if (error) return <div>Error</div>
        
                        data = data["getAllScenarios"];
                        data = data.filter((item) => item.id !== null && item.id !== undefined);
                        return (
                            <div>
                                <ScenarioPageModal data={data} addName={handleAddName} removeName={handleRemoveName} checkedItems={checkedItems} setCheckedItems={setCheckedItems}/>
                                <Paper className='paper-container'>
                                    <TableContainer style={{ maxHeight: '70vh' }}>
                                        <Table stickyHeader aria-label="simple table">
                                            <TableHead>
                                                <TableRow>
                                                    <TableCell className="tableCell main">Scenarios</TableCell>
                                                </TableRow>
                                            </TableHead>
                                            <TableBody>
                                                {data.map((item, index) => (
                                                    checkedItems.includes(item.id) &&
                                                    <TableRow key={index}style={{ backgroundColor: index % 2 === 0 ? '#f4f4f4' : '#fafafa' }}>
                                                        <TableCell className="tableCell main">{renderNestedItems(item)}</TableCell>
                                                    </TableRow>
                                                ))}
                                            </TableBody>
                                        </Table>
                                    </TableContainer>
                                </Paper>
                            </div>
                        );
                    }
                }
            </Query>
        );
    }

    return (
        <MainTable />
    );
    
}

export default ScenarioPage;
