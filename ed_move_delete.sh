#!/bin/bash

# Check for arguments
if [ "$#" -ne 1 ]; then
    echo "Usage: ./run.sh <folder_name>"
    exit 1
fi

# Find the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"


# Run the Python script using its absolute path
python3 "$SCRIPT_DIR/src/ed_move_delete.py" "$@"

echo "Mirroring completed."
