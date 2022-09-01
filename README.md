# OBS Monitor Audio

Monitor Audio is an [OBS Studio](https://obsproject.com/) script that sets the audio output for sources (current and new) to be monitored to the default audio output of the system. This is generally used in scenarios where OBS is projected onto a screen and audio is desired to be routed into the sound system the computer is connected to. Certain sources can optionally be ignored for monitoring by name.

Keep the OBS "Script Log" open to confirm the sources set to monitor audio.


## OBS Scripting Setup

The OBS Monitor Audio script requires [OBS Studio](https://obsproject.com/) and Python 3.6+. OBS Studio supports current Python versions now on Windows, so grab the latest stable "Windows installer (64-bit)" build available at [python.org](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe). From the OBS Studio software, select "Tools" from the menu bar and "Scripts" from the menu, go to the "Python Settings" tab, and select the base prefix for Python 3.6+. For Windows, the base prefix will be `%LOCALAPPDATA%\Programs\Python\Python310` (for Python 3.10). To load one of the scripts below, go back to the "Scripts" tab and click the "+" in the lower-left and navigate to the appropriate script file.


## Usage

Load `monitor-audio.py` into OBS Studio (if not already loaded). No other setup is required as this plugin will proceed to automatically monitor all current and new sources in scenes as they are staged/shown. Sources to ignore can be specified in a list in the script settings by source name.
