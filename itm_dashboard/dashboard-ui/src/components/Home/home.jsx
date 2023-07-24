import React from 'react';
import ScoreChart from '../Home/scoreChart';
import { Query } from 'react-apollo';
import gql from 'graphql-tag';

const getScenarioNamesQueryName = "getScenarioNames";

const scenario_names_aggregation = gql`
    query getScenarioNames{
        getScenarioNames
  }`;

class HomePage extends React.Component {

    getHeaderLabel(id, name) {
        if(id.indexOf("ADEPT1") > -1 ) {
            return ("BBN: " + id + " " + name);
        } else {
            return ("Soartech: " + id + " " + name);
        }
    }

    render() {
        return (
            <Query query={scenario_names_aggregation}>
            {
                ({ loading, error, data }) => {
                    if (loading) return <div>Loading ...</div> 
                    if (error) return <div>Error</div>

                    const scenarioNameOptions = data[getScenarioNamesQueryName];
                    let scenariosArray = [];
                    for(let i=0; i < scenarioNameOptions.length; i++) {
                        scenariosArray.push({
                            "id": scenarioNameOptions[i]._id.id, 
                            "name": scenarioNameOptions[i]._id.name
                        });
                    }
                    scenariosArray.sort((a, b) => (a.id > b.id) ? 1 : -1);

                    return (
                        <div className="home-container">
                             {
                                scenariosArray.map(scenario =>
                                    <div className='chart-home-container' key={"id_" +scenario.id}>
                                        <div className='chart-header'>
                                            <div className='chart-header-label'>
                                                <h4>{this.getHeaderLabel(scenario.id, scenario.name)}</h4>
                                            </div>
                                        </div>
                                        <ScoreChart testid={scenario.id}/>
                                    </div>
                                )
                            }
                        </div>
                    )
                }
            }
            </Query>
            
        );
    }
}

export default HomePage;