import React, { useState, useEffect } from 'react';
import { ResponsiveBar } from '@nivo/bar';
import { useQuery } from '@apollo/react-hooks';
import gql from 'graphql-tag';

const GET_ALL_ITM_SIMULATIONS = gql`
    query getAllHistory($id: ID!) {
        getAllHistory(id: $id)
    }`;

// This is all just using age from demographics to make a testing score and proving that we can access the database
// Actual scoring needs to change!
const ScoreChart = () => {
    const [alignmentScoreTotal, setAlignmentScoreTotal] = useState({});
    const { loading, error, data } = useQuery(GET_ALL_ITM_SIMULATIONS, { variables: { "id": "Testing_12345" } });

    useEffect(() => {
        if (data && data.getAllHistory) {
            mapData(data.getAllHistory);
        }
    }, [data]);

    const mapData = (data) => {
        let newScores = {...alignmentScoreTotal};
        data.map((item) => {
            if (item.history[0].response.hasOwnProperty("state")) {
                const performer = item.history[0].parameters["adm_name"];
                const prevPerformerData = newScores[performer] || { total: 0, count: 0 };
                newScores[performer] = {
                    total: prevPerformerData.total + item.history[0]["response"]["state"]["casualties"][0]["demographics"]["age"],
                    count: prevPerformerData.count + 1,
                };
            }
        });
        setAlignmentScoreTotal(newScores);
    }

    const mappedArray = Object.entries(alignmentScoreTotal).map(([performer, { total, count }]) => ({
        performer,
        "Average Alignment Score": count !== 0 ? (total / count/ 100).toFixed(2) : 0
    }));

    if (loading) return <div>Loading ...</div>
    if (error) return <div>Error</div>

    return (
        <div className="score-chart-container">
            <ResponsiveBar
                data={mappedArray}
                keys={['Average Alignment Score']}
                indexBy="performer"
                margin={{ top: 50, right: 130, bottom: 50, left: 80 }}
                padding={0.4}
                layout="horizontal"
                valueScale={{ type: 'linear', min: 0, max: 1 }}
                indexScale={{ type: 'band', round: true }}
                colors={['#ff82d8', '#14b7d0']}
                colorBy="index"
                borderColor={{ from: 'color', modifiers: [['darker', 1.6]] }}
                borderWidth={0.2}
                axisTop={null}
                axisRight={null}
                axisBottom={{
                    tickSize: 5,
                    tickPadding: 5,
                    tickRotation: 0,
                    legend: 'Average Alignment Score',
                    legendPosition: 'middle',
                    legendOffset: -40,
                }}
                labelSkipWidth={12}
                labelSkipHeight={12}
                labelTextColor="black"
                animate={true}
                motionStiffness={90}
                motionDamping={15}
            />
        </div>
    );
};

export default ScoreChart;
