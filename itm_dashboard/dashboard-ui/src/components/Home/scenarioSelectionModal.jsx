import React, { useState } from 'react';
import Dialog from '@material-ui/core/Dialog';
import DialogTitle from '@material-ui/core/DialogTitle';
import DialogContent from '@material-ui/core/DialogContent';
import Button from '@material-ui/core/Button';
import FormControl from '@material-ui/core/FormControl';
import MenuItem from '@material-ui/core/MenuItem';
import Select from '@material-ui/core/Select';
import InputLabel from '@material-ui/core/InputLabel';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
    paper: {
      maxWidth: '800px',
    },
}));

const HomeChartModal = ({ data, selectedADMName, selectedId, handleADMNameChange, handleIdChange }) => {
    const [open, setOpen] = useState(false);
    const handleClickOpen = () => {
        setOpen(true);
    };
    const handleClose = () => {
        setOpen(false);
    };
    const classes = useStyles();

    return (
        <div className='center-div'>
            <Button variant="outlined" color="primary" onClick={handleClickOpen}>
                Select ITM Simulation ID
            </Button>
            <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title" classes={{paper: classes.paper}}>
                <DialogTitle id="form-dialog-title">Select ITM Simulation History</DialogTitle>
                <DialogContent>
                    <FormControl className="home-table">
                        <InputLabel id="ADMName-select-label" shrink>Select ADMName</InputLabel>
                        <Select
                            labelId="ADMName-select-label"
                            id="ADMName-select"
                            value={selectedADMName}
                            onChange={handleADMNameChange}
                            displayEmpty
                        >
                            <MenuItem value="">None</MenuItem>
                            {
                                Array.from(new Set(data.map(item => item.history[0].parameters["ADM Name"]))).map((ADMName, index) => (
                                    <MenuItem value={ADMName} key={index}>{ADMName}</MenuItem>
                                ))
                            }
                        </Select>
                    </FormControl>
                    <FormControl className="home-table">
                        <InputLabel id="id-select-label" shrink>Select ITM Simulation History</InputLabel>
                        <Select
                            labelId="id-select-label"
                            id="id-select"
                            value={selectedId}
                            onChange={handleIdChange}
                            displayEmpty
                        >
                            <MenuItem value="">None</MenuItem>
                            {
                                data.filter(item => item.history[0].parameters["ADM Name"] === selectedADMName).map((item, index) => (
                                    <MenuItem value={item._id} key={index}>{item.history[0].response.id}</MenuItem>
                                ))
                            }
                        </Select>
                    </FormControl>
                </DialogContent>
            </Dialog>
        </div>
    );
}

export default HomeChartModal;
