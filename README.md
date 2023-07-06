# In the Moment (ITM) - MVP

This README provides a guide to setup and run the ITM application.

## To-Dos
* Return error codes from server as per API documentation
* Move scenario selection to configuration and/or command-line arguments


## Prerequisites

Ensure you have Python 3.10 installed on your system. If you don't have it installed, you can download it from the [official Python website](https://www.python.org/downloads/).

## Setup

1. First, we need to setup a Python virtual environment. Navigate to the directory where you cloned the repository and run the following command to create a new virtual environment:

```
python3.10 -m venv venv
```


2. Activate the newly created virtual environment with:

```
source venv/bin/activate
```


## Installation

Once you're in the virtual environment, you're ready to install the necessary Python packages for the project. From the `itm_server` directory, run:

```
pip install -r requirements.txt
```
    

## Running the Server

After the installation is complete, you can start the server. From the `itm_server` directory, start the server by running:

```
python3 -m swagger_server
```

## Running the ADM minimal runner

To interact with the server, you will need to run a client. Please ensure that the server is running before you start a client. To see additional details regarding modifying this minimal runner to be a TA2 client, see the comments at the top of `itm_minimal_runner.py`.  To run it, open a new terminal, activate your virtual environment and inside the `itm_client` directory run `itm_minimal_runner.py`:

```
usage: itm_minimal_runner.py [-h] --adm_name ADM_NAME [--session [session_type [scenario_count ...]]] [--eval]

Runs ADM scenarios.

options:
  -h, --help            show this help message and exit
  --adm_name ADM_NAME   Specify the ADM name
  --session [session_type [scenario_count ...]]
                        Specify session type and scenario count. Session type can be test, adept, or soartech. If you want to run through all available scenarios without repeating do not use the scenario_count argument
  --eval                Run an evaluation session. Supercedes --session and is the default if nothing is specified. Implies --db.
```

## Running the Human input simulator
 
To interact with the server, you will need to run a client. Please ensure that the server is running before you start a client. Open a new terminal, activate your virtual environment and inside the `itm_client` directory run `itm_human_input.py`:

```
usage: itm_human_input.py [-h] [--db] [--session [session_type [scenario_count ...]]] [--eval]

Runs Human input simulator.

options:
  -h, --help            show this help message and exit
  --db                  Put the output in the MongoDB (ensure that the itm_dashboard docker container is running) and save a json output file locally inside itm_server/itm_mvp_local_output/
  --session [session_type [scenario_count ...]]
                        Specify session type and scenario count. Session type can be test, adept, or soartech. If you want to run through all available scenarios without repeating do not use the scenario_count argument
  --eval                Run an evaluation session. Supercedes --session and is the default if nothing is specified. Implies --db.
```


## End of Instructions

If you've followed these steps, you should now have the ITM server and at least one client running.
