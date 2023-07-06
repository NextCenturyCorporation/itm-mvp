import React, { useState } from 'react';
import Dialog from '@material-ui/core/Dialog';
import DialogTitle from '@material-ui/core/DialogTitle';
import DialogContent from '@material-ui/core/DialogContent';
import Button from '@material-ui/core/Button';
import FormControl from '@material-ui/core/FormControl';
import MenuItem from '@material-ui/core/MenuItem';
import Select from '@material-ui/core/Select';
import InputLabel from '@material-ui/core/InputLabel';
import Checkbox from '@material-ui/core/Checkbox';
import ListItemText from '@material-ui/core/ListItemText';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
    paper: {
      maxWidth: '800px',
    },
    scenarioButton: {
        margin: theme.spacing(0.5)
    }
  }));

const ScenarioPageModal = ({ data, checkedItems, setCheckedItems }) => {
    const [open, setOpen] = useState(false);

    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };

    const handleChange = (event) => {
        setCheckedItems(event.target.value);
    };

    const handleSelectAll = () => {
        const allItems = data
            .filter((item, index, self) => self.findIndex((i) => i.id === item.id) === index)
            .map((item) => item.id)
        setCheckedItems(allItems);
    };

    const handleClear = () => {
        setCheckedItems([]);
    };


    const classes = useStyles();

    return (
        <div className='center-div'>
            <Button variant="outlined" color="primary" onClick={handleClickOpen}>
                Select Scenarios
            </Button>
            <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title" classes={{paper: classes.paper}}>
                <DialogTitle id="form-dialog-title">Select Scenarios</DialogTitle>
                <DialogContent>
                    <FormControl className="home-table">
                        <InputLabel id="scenario-name-select-label" shrink>Select Username</InputLabel>
                            <Select
                                labelId="scenario-name-select-label"
                                id="scenario-name-select"
                                multiple
                                value={checkedItems}
                                onChange={handleChange}
                                displayEmpty
                                renderValue={(selected) => `Selected ${selected.length}`}
                            >
                                {
                                    data
                                    .filter((item, index, self) => self.findIndex((i) => i.id === item.id) === index)
                                    .map((item) => (
                                    <MenuItem value={item.id} key={item.id}>
                                        <Checkbox checked={checkedItems.includes(item.id)} />
                                        <ListItemText primary={item.id} />
                                    </MenuItem>
                                    ))
                                }
                            </Select>
                        <Button className={classes.scenarioButton} variant="contained" color="primary" onClick={handleSelectAll}>Select All</Button>
                        <Button className={classes.scenarioButton} variant="contained" color="secondary" onClick={handleClear}>Clear Selection</Button>
                    </FormControl>
                </DialogContent>
            </Dialog>
        </div>
    );
}

export default ScenarioPageModal;
