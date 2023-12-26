#!/bin/bash

# Install Homebrew if not present
if ! command -v brew &> /dev/null
then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install Python3 if not present
if ! command -v python3 &> /dev/null
then
    echo "Installing Python3..."
    brew install python
fi

# Install ImageMagick
echo "Installing ImageMagick..."
brew install imagemagick

# Install Pillow for Python
echo "Installing Python dependencies..."
pip3 install Pillow

echo "Setup completed successfully."


# More setup
# Making scripts executable
chmod +x ed_move_delete.sh
chmod +x ed_copy_resize.sh

# Adding script directory to PATH
SCRIPT_DIR="$(pwd)"
echo "export PATH=\"\$PATH:$SCRIPT_DIR\"" >> ~/.bashrc
echo "export PATH=\"\$PATH:$SCRIPT_DIR\"" >> ~/.zshrc

# Reload shell configuration
source ~/.bashrc || source ~/.zshrc

echo "Setup completed and scripts added to PATH."