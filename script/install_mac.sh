#!/usr/bin/env bash


# This script will add the EachPy source directory to the PTHONPATH variable.
# After that from any python script just import EachPy.SomeModule etc...

# Run the script to modify PYTHONPATH
./install_helper.sh

# Determine which shell profile to use
if [ -n "$ZSH_VERSION" ]; then
    shell_config_file="$HOME/.zshrc"
else
    shell_config_file="$HOME/.bash_profile"
fi

# Source the shell configuration file to apply changes
source "$shell_config_file"
echo "Sourced $shell_config_file to apply changes to PYTHONPATH."
