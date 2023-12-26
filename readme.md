# Image Processing Scripts

These scripts were made for Danie Terblanche Photography, with the purpose of removing the lag from interactive image sorting. It's currently a 3 step process, in the first step a smaller mirror of the image directory is made that enables easy image manipulation. The user then moves and deletes images in the small folder. Once satisfied, the user can choose to mirror these changes back to the original folder.

## Description
This package contains two scripts for managing and processing image files:
- `copy_resize.sh`: Resizes images in a specified directory and converts them to JPEG format, storing them in a new directory with `_small` appended to the name.
- `move_delete.sh`: Mirrors file operations like move and delete from the `_small` directory back to the original directory.

## Setup Procedure
0. Ensure that home brew is installed. Instructions [here](https://stackoverflow.com/questions/66666134/how-to-install-homebrew-on-m1-mac).
1. Clone or download this repository to your local machine.
```
git clone git@github.com:eduardkieser/ed_copy_delete.git
```
2. Open a terminal and navigate to the directory containing the scripts.
3. Run the setup script: `zsh ./ed_setup.sh`. This installs necessary dependencies, makes the scripts executable, and adds them to your PATH.
4. Restart your terminal or source your shell configuration file to apply PATH changes.

## Usage
1. **Resizing and Converting Images**: Run `copy_resize.sh <folder_name>`. This creates a copy of your specified folder, appending `_small` to the folder name, with resized and converted images. You can run this file multiple time to be sure.
2. **Modifying Images**: Manually move and delete images in the `<folder_name>_small` directory as needed.
3. **Mirroring Changes**: After modifying images in the `_small` folder, run `move_delete.sh <original_folder_name>` to apply these changes back to the original folder.

### Notes
- Ensure you have internet access during the setup.
- Requires a Mac with Homebrew and Python.
- Make sure you have a backup, if things go wrong you may loose a lot of pictures!