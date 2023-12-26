#!/bin/bash

# Check for arguments
if [ "$#" -ne 1 ]; then
    echo "Usage: ./run.sh <folder_name>"
    exit 1
fi

# Resize and convert images
python3 ed_copy_resize.py "$1"

echo "Copy resize is done."
