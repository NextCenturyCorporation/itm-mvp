import React from 'react';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';

const AlignmentScoreBox = ({ performer }) => {
  const score = Math.random().toFixed(2);

  return (
    <Box className="scoreBox">
      <Typography variant="h6">
        {performer}
        <br />
      </Typography>
      <Typography variant="h6">
        {score}
      </Typography>
    </Box>
  );
}

export default AlignmentScoreBox;
