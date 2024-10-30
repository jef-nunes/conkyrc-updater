### About
*What this program does:*
Takes a list of paths for user custom conky configuration files and overwrites the user scope ~/.conkyrc file with the content from the selected custom file. In the settings.py insert the paths for your custom conkyrc files and adjust path for backup file.

### Running
Call script providing argument with the index of selected conkyrc file inside the settings.py list.
For also running conky after changes, pass the --run flag.

Examples:<br>
**1. Pass the first element on settings.py path list**
```sh
python3 conkyrc_updater.py 0
```
**2. Also running conky application:**
```sh
python3 conkyrc_updater.py 0 --run
```
