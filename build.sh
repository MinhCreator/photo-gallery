#!/bin/bash

# install python3
sudo apt install python3

# Define the project directory
PROJECT_DIR=$(pwd)
echo "Project directory: $PROJECT_DIR"

# Define the virtual environment directory
VENV_DIR=${PROJECT_DIR}/venv
echo "Virtual environment directory: $VENV_DIR"

# Create a virtual environment if it doesn't exist
echo "Creating virtual environment in $VENV_DIR please keep waiting..."
if [ ! -d "$VENV_DIR" ]; then
  python -m venv $VENV_DIR
fi

# Creating upload folder if it doesn't exist
UPLOAD_DIR=${PROJECT_DIR}/static/upload_image

if [ ! -d "$UPLOAD_DIR" ]; then
  mkdir $UPLOAD_DIR
  echo "upload folder created"
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

# Install dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the main application
echo "deploying application..."
python3 main.py