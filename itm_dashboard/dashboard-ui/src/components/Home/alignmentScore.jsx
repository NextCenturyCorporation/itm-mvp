import React from 'react';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';

const AlignmentScoreBox = ({ performer, data }) => {
  const score = data.history[data.history.length - 1].response.score.toFixed(4);

  return (
    <Box className="scoreBox">
      <Typography variant="h5">
        {performer}
        <br />
      </Typography>
      <Typography variant="h5">
        Alignment Score: {score}
      </Typography>
    </Box>
  );
}

export default AlignmentScoreBox;
