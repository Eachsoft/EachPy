#!/usr/bin/env bash

# Function to add the current directory to PYTHONPATH in the shell profile file
add_current_directory_to_pythonpath() {
    # Determine which shell profile to use
    local shell_config_file
    if [ -n "$ZSH_VERSION" ]; then
        shell_config_file="$HOME/.zshrc"
    else
        shell_config_file="$HOME/.bash_profile"
    fi

    # Get the current directory
    # Get the current working directory
    current_directory=$(pwd)

    # Get the parent directory of the current working directory
    parent_directory=$(dirname "$current_directory")

    local directory="$parent_directory/Source"

    # Create the shell profile file if it doesn't exist
    touch "$shell_config_file"

    # Check if the directory is already in PYTHONPATH
    if grep -q "PYTHONPATH.*$directory" "$shell_config_file"; then
        echo "Directory '$directory' is already in PYTHONPATH in $shell_config_file"
    else
        echo "Adding '$directory' to PYTHONPATH in $shell_config_file"
        echo "export PYTHONPATH=\"\$PYTHONPATH:$directory\"" >> "$shell_config_file"
        echo "Added '$directory' to PYTHONPATH. Please restart your terminal or run 'source $shell_config_file' to apply changes."
    fi
}

# Call the function to add the current directory to PYTHONPATH
add_current_directory_to_pythonpath
