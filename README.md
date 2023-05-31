# In The Moment (ITM) - MVP

This README provides a guide to setup and run the Item Management (ITM) application.

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
python -m swagger_server
```


## Running the Client
 
To interact with the server, you will need to run the client. Please ensure that the server is running before you start the client. Open a new terminal, activate your virtual environment and inside the `itm_client` directory run:

```
python itm_human_input.py
```


## End of Instructions

If you've followed these steps, you should now have the ITM server and client running.
