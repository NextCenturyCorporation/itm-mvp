import React from 'react';
import { useState } from 'react';
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import TableContainer from "@material-ui/core/TableContainer";
import Paper from '@material-ui/core/Paper';
import ScenarioSelectionModal from './scenarioSelectionModal';
import AlignmentScoreBox from './alignmentScore';

import { Query } from 'react-apollo';
import gql from 'graphql-tag';

const GET_ALL_ITM_SIMULATIONS = gql`
    query getAllHistory($id: ID!) {
        getAllHistory(id: $id)
    }`;


const snakeCaseToNormalCase = (string) => {
    return string
        .replace(/_/g, ' ')
        .replace(/(^\w|\s\w)/g, m => m.toUpperCase());
}

const HomeTable = () => {
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
                    <TableRow key={i}>
                        <TableCell className="tableCell">
                            <strong>{snakeCaseToNormalCase(key)}</strong>
                        </TableCell>
                        <TableCell className="tableCell">{renderNestedItems(value)}</TableCell>
                    </TableRow>
                ))}
            </TableBody>
        </Table>
    );
    
    const MainTable = () => {
        const [selectedId, setSelectedId] = useState("");
        const [selectedADMName, setSelectedADMName] = useState("");

        const handleADMNameChange = (event) => {
            setSelectedADMName(event.target.value);
            setSelectedId("");
        };

        const handleIdChange = (event) => {
            setSelectedId(event.target.value);
        };


        return (
            <Query query={GET_ALL_ITM_SIMULATIONS} variables={{ "id": "Testing_12345" }}>
                {
                    ({ loading, error, data }) => {
                        if (loading) return <div>Loading ...</div> 
                        if (error) return <div>Error</div>
        
                        data = data["getAllHistory"];
                        let selectedItem = data.find(item => item.history[0].response.id === selectedId);
                        return (
                            <div>
                                <div className='center-div'>
                                    <ScenarioSelectionModal 
                                        data={data}
                                        selectedADMName={selectedADMName}
                                        selectedId={selectedId}
                                        handleADMNameChange={handleADMNameChange}
                                        handleIdChange={handleIdChange}
                                    />
                                </div>
                                {selectedItem &&
                                    <div>
                                        <AlignmentScoreBox performer={selectedADMName}/>
                                        <Paper className='paper-container'>
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
                                                        {selectedItem.history.map((item, index) => (
                                                            <TableRow key={index}>
                                                                <TableCell className="tableCell main">{item.command}</TableCell>
                                                                <TableCell className="tableCell main">{renderNestedItems(item.parameters)}</TableCell>
                                                                <TableCell className="tableCell main">{renderNestedItems(item.response)}</TableCell>
                                                            </TableRow>
                                                        ))}
                                                    </TableBody>
                                                </Table>
                                            </TableContainer>
                                        </Paper>
                                    </div>
                                }
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

export default HomeTable;
