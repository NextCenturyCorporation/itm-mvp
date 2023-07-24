import React from 'react';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';

const AlignmentScoreBox = ({ performer, data, scenario }) => {
  let score = "Not Available"
  let sessionId = null;

  if(data.history !== null && data.history !== undefined) {
    if( data.history[data.history.length - 1].response.score !== undefined) {
        score = data.history[data.history.length - 1].response.score.toFixed(4);
    }

    for(let i=0; i < data.history.length - 1; i++) {
      if(data.history[i].command === "TA1 Alignment Target Session ID") {
        sessionId = data.history[i].response; 
      }
    }
  }

  return (
    <Box className="scoreBox">
      <Typography variant="h5">
        {performer}
        <br />
      </Typography>
      <Typography variant="h5">
        Alignment Score: {score}
        {scenario === 'kickoff-demo-scenario-1' && 
          <iframe src={"http://localhost:8084/graph/session/" + sessionId} title="SoarGraph" width="800px" height="800px"></iframe>
        }
      </Typography>
    </Box>
  );
}

export default AlignmentScoreBox;
