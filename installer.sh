#!/bin/bash

RAW_URL="https://raw.githubusercontent.com/chamster24/Crostini-Killer/main/files"

# Make the folder
mkdir -p ~/.cH24-Apps/Crostini-Killer/

sudo apt update && sudo apt install -y python3
echo "Installed Python3"

# Copy the python script
curl -sSL "$RAW_URL/crostini-killer.py" -o ~/.cH24-Apps/Crostini-Killer/crostini-killer.py
chmod +x ~/.cH24-Apps/Crostini-Killer/crostini-killer.py
echo "Crostini-Killer Installed/Updated!"

# check to see if the config file is already there
if [ ! -f ~/.cH24-Apps/Crostini-Killer/crostini-killer-config.csv ]; then
  curl -sSL "$RAW_URL/crostini-killer-Config.csv" -o ~/.cH24-Apps/Crostini-Killer/crostini-killer-config.csv
  echo "Installed template config file!"
fi

# checks for shortcut, if no, prompts to install
if [ ! -f $HOME/.local/share/applications/crostini-killer.desktop ]; then
  SHORTCUT_PATH=$HOME/.local/share/applications/crostini-killer.desktop
  echo "Would you like to add a shortcut to the taskbar? (type 'Y' if you do)"
    read -n 1 -r  # waits for 1 character
    echo ""       # Move to a new line after the keypress
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Adding shortcut!"
        mkdir -p ~/.local/share/icons/
        curl -sSL "$RAW_URL/icon.png" -o ~/.cH24-Apps/Crostini-Killer/icon.png
        APP_DIR="$HOME/.cH24-Apps/Crostini-Killer"
        SHORTCUT_PATH="$HOME/.local/share/applications/crostini-killer.desktop"
cat <<EOF > "$SHORTCUT_PATH"
[Desktop Entry]
Name=Crostini Killer
Comment=User-friendly task manager app
Exec=bash -c "cd $APP_DIR && python3 crostini-killer.py; echo '----------------'; read -p 'Task Complete. Press Enter to exit.' -r"
Icon=$APP_DIR/icon.png
Terminal=true
Type=Application
Categories=System;
EOF

chmod +x "$SHORTCUT_PATH"
    else
        echo "Skipped."
    fi
fi

echo "Download finished!"
