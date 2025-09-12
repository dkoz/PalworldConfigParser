# Palworld Config Parser
This tool updates the `PalworldSettings.ini` configuration file by replacing its values with corresponding environment variables.

I based this tool on the one create by Quinten for Pterodactyl. Just supports a wider range of settings that otherwise weren't working on the original.

## Build Instructions

### Linux
```
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install pyinstaller
pyinstaller --onefile ConfigParser.py
```

### Windows
```
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install pyinstaller
pyinstaller --onefile ConfigParser.py
```