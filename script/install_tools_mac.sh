#!/usr/bin/env bash


./install_tools_helper.sh

if [ -n "$ZSH_VERSION" ]; then
    shell_config_file="$HOME/.zshrc"
else
    shell_config_file="$HOME/.bash_profile"
fi

source "$shell_config_file"
echo "Sourced $shell_config_file to apply changes to PATH."
