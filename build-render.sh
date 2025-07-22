#!/bin/bash

# Creating upload folder if it doesn't exist
UPLOAD_DIR=${PROJECT_DIR}/static/upload_image

if [ ! -d "$UPLOAD_DIR" ]; then
  mkdir $UPLOAD_DIR
  echo "upload folder created"
fi

# Run the main application
echo "deploying application..."
python3 main.py