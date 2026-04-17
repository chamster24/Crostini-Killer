#!/bin/bash

# Make the folder
mkdir -p ~/.cH24-Apps/Crostini-Killer/

# Copy the python script
cp /files/crostini-killer.py ~/.cH24-Apps/Crostini-Killer/
echo "Crostini-Killer Installed/Updated!"

# check to see if the config file is already there
if [ ! -f ~/.cH24-Apps/Crostini-Killer/crostini-killer-config.csv ]; then
  cp /files/crostini-killer-config.csv ~/.cH24-Apps/Crostini-Killer/
  echo "Installed template config file!"
fi

# checks for shortcut, if no, prompts to install
if [ ! -f $HOME/.local/share/applications/crostini-killer.desktop ]; then
  SHORTCUT_PATH=$HOME/.local/share/applications/crostini-killer.desktop
  echo "Would you like to add a shortcut to the taskbar?"
    read -n 1 -r  # waits for 1 character
    echo ""       # Move to a new line after the keypress
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Adding shortcut!"
        cp /files/icon.png ~/.cH24-Apps/Crostini-Killer/
cat <<EOF > "$SHORTCUT_PATH"
[Desktop Entry]
Name=Crostini Killer
Comment=User-friendly task manager app
Exec=python3 $HOME/.cH24-Apps/Crostini-Killer/crostini-killer.py
Icon=$HOME/.cH24-Apps/Crostini-Killer/icon.png
Terminal=true
Type=Application
Categories=System;
EOF
    else
        echo "Skipped."
    fi
fi

echo "Download finished!"
