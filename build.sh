#!/bin/bash

# Define the project directory
PROJECT_DIR=$(pwd)

# Define the virtual environment directory
VENV_DIR=${PROJECT_DIR}/venv

# Create a virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
  python -m venv $VENV_DIR
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run the main application
python main.py