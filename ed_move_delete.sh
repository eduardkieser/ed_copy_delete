#!/bin/bash

# Check for arguments
if [ "$#" -ne 1 ]; then
    echo "Usage: ./run.sh <folder_name>"
    exit 1
fi

# Mirror file operations
python3 ed_move_delete.py "$1"

echo "Mirroring completed."
