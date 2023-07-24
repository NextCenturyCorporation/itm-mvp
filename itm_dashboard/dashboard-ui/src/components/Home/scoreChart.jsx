import React from 'react';
import { ResponsiveBar } from '@nivo/bar';
import gql from 'graphql-tag';
import { Query } from 'react-apollo';

const GET_HISTORIES_BY_ID = "getAllHistoryByID";
const get_all_history_by_id = gql`
    query getAllHistoryByID($historyId: ID) {
        getAllHistoryByID(historyId: $historyId)
    }`;

const formatLeftIndexString = function(peformerADMString) {
    if(peformerADMString.indexOf("ALIGN-ADM") > -1 ) {
        return ("Kitware: " + peformerADMString);
    } else if (peformerADMString.indexOf("TAD") > -1){
        return ("Parallax: " + peformerADMString);
    } else {
        return peformerADMString;
    }
}

const MyResponsiveBar = ({mappedArray}) => {
    return (
        <div className="score-chart-container">
            <ResponsiveBar
                data={mappedArray}
                keys={['Average Alignment Score']}
                indexBy="performer"
                margin={{ top: 50, right: 50, bottom: 50, left: 160 }}
                padding={0.4}
                layout="horizontal"
                valueScale={{ type: 'linear', min: 0, max: 1 }}
                indexScale={{ type: 'band', round: true }}
                colors={['#00A0D2', "#999D5D"]}
                colorBy="index"
                borderColor={{ from: 'color', modifiers: [['darker', 1.6]] }}
                borderWidth={0.2}
                axisTop={null}
                axisRight={null}
                axisLeft={{ format: v => formatLeftIndexString(v) }}
                axisBottom={{
                    tickSize: 5,
                    tickPadding: 5,
                    tickRotation: 0,
                    legend: 'Alignment Score',
                    legendPosition: 'middle',
                    legendOffset: -10,
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

class ScoreChart extends React.Component {

    constructor(props) {
        super(props);

        this.state = { 
            style: {fontFamily: "Lato", textAlign: "center"}
        }
    }

    render() {
        return (
            <Query query={get_all_history_by_id} variables={{"historyId": this.props.testid}}>
            {
                ({ loading, error, data }) => {
                    if (loading) return <div>No stats yet</div> 
                    if (error) return <div>Error</div>

                    const chartData = data[GET_HISTORIES_BY_ID];

                    let newScores = {};
                    const scores = chartData.map((item) => {
                        const performer = item.history[0].parameters["ADM Name"];
                        const prevPerformerData = newScores[performer] || { total: 0, count: 0 };
                        newScores[performer] = {
                            total: prevPerformerData.total + item.history[item.history.length - 1].response.score,
                            count: prevPerformerData.count + 1,
                        };

                        return newScores;
                    });

                    const mappedArray = Object.entries(newScores).map(([performer, { total, count }]) => ({
                        performer,
                        "Average Alignment Score": count !== 0 ? (total / count).toFixed(4) : 0
                    }));

                    mappedArray.sort((a, b) => (a.performer > b.performer) ? -1 : 1);

                    return (
                        <div style={this.state.styles} className="flex-chart-center">
                            <div className="results-chart-container">
                                <MyResponsiveBar mappedArray={mappedArray}/>
                            </div>
                        </div>

                    )
                }
            }
            </Query>
        );
    }
}

export default ScoreChart;
