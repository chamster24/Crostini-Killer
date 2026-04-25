# Crostini-Killer
A killer for linux (designed for Crostini) apps

Installation Options:
- Download from latest release: run in terminal the following `bash <(curl -sSL "https://raw.githubusercontent.com/chamster24/Crostini-Killer/main/fetch.sh")`
  - Once installed, run in the terminal `crostini-killer` to run it (the shortcut doesn't work right now)

- Download from latest release's .deb: run in terminal the following `wget [https://github.com/chamster24/Crostini-Killer/releases/latest/download/crostini-killer.deb](https://github.com/chamster24/Crostini-Killer/releases/latest/download/crostini-killer.deb) && sudo apt install ./crostini-killer.deb -y && rm crostini-killer.deb`

- Manual Download:
  - Download the latest .deb from the [Releases page](https://github.com/chamster24/Crostini-Killer/releases/latest)
  - Locate the file in your downloads. If on a Chromebook, drag it into the "Linux files" folder.
  - Right-click crostini-killer.deb and select "Install with Linux" (or open with "Software Install" on Ubuntu/Debian).
  - Launch "Crostini Killer" from your App Drawer/Start Menu.

To uninstall if you installed via the .deb:
- Run `sudo apt remove crostini-killer` in your terminal
