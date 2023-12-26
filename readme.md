# Image Processing Scripts

## Description
This package contains two scripts for image processing:
- `copy_resize.sh`: Resizes images and converts them to JPEG format.
- `move_delete.sh`: Mirrors file operations (move and delete) from a '_small' directory to the original.

## Setup Procedure
1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the directory containing the scripts.
3. Run the setup script: `./ed_setup.sh`. This will install necessary dependencies, make the scripts executable, and add them to your PATH.
4. Close and reopen your terminal, or run `source ~/.bashrc` (or `source ~/.zshrc` for zsh users) to apply the PATH changes.

## Usage
- To resize and convert images, run: `copy_resize.sh <folder_name>`.
- To mirror file operations, run: `move_delete.sh <original_folder_name>`.

### Notes
- Ensure you have internet access during the setup.
- Requires a Mac with internet access.
