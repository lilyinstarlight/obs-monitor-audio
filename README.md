# OBS Monitor Audio

Monitor Audio is an [OBS Studio](https://obsproject.com) script that sets the audio output for all sources (current and new) to be monitored to the default audio output for the system. This is generally used in scenarios where OBS is projected onto a screen and audio is desired to be routed into the sound system the computer is connected to.

Keep the OBS "Script Log" open to confirm the sources set to monitor audio.


## OBS Scripting Setup

The FTC Match Uploader script requires [OBS Studio](https://obsproject.com/) and Python 3.6+. OBS Studio only supports Python 3.6 on Windows currently and the latest Windows installer available is [Python 3.6.8](https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe). From the OBS Studio software, select "Tools" from the menu bar and "Scripts" from the menu, go to the "Python Settings" tab, and select the base prefix for Python 3.6+. For Windows, the base prefix will be `%LOCALAPPDATA%\Programs\Python\Python36`. To load one of the scripts below, go back to the "Scripts" tab and click the "+" in the lower-left and navigate to the appropriate script file.


## Usage

Load `monitor-audio.py` into OBS Studio (if not already loaded). No other setup is required as this plugin will proceed to automatically monitor all current and new sources in scenes as they are staged/shown.
