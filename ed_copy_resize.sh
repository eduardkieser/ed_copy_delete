#!/bin/bash

# Check for arguments
if [ "$#" -ne 1 ]; then
    echo "Usage: ./ed_copy_resize.sh <folder_name>"
    exit 1
fi

# Find the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Resize and convert images
python3 "$SCRIPT_DIR/src/ed_copy_resize.py" "$@"

echo "Copy resize is done."
