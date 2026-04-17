#!/bin/bash

REPO="chamster24/Crostini-Killer"
# Get the tag name of the latest stable release
LATEST=$(curl -s https://api.github.com/repos/$REPO/releases/latest | grep "tag_name" | cut -d '"' -f 4)
# Run the installer
curl -sSL "https://raw.githubusercontent.com/$REPO/$LATEST/installer.sh" | bash
