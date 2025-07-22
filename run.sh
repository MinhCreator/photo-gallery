#!/bin/bash

# Define the project directory
PROJECT_DIR=$(pwd)
echo "Project directory: $PROJECT_DIR"

# Creating upload folder if it doesn't exist
UPLOAD_DIR=${PROJECT_DIR}/static/upload_image

if [ ! -d "$UPLOAD_DIR" ]; then
  mkdir $UPLOAD_DIR
  echo "upload folder created"
fi
