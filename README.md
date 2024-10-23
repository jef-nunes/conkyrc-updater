### About
*What this program does:*
Takes a list of paths for user custom conky configuration files and overwrites the user scope ~/.conkyrc file with the content from the selected custom file.

### Modify settings
In the settings.py insert the paths for your custom conkyrc files and adjust other paths as needed.

### Running
On script call, include a first argument with the index of selected conkyrc file, relative to its position on settings.py list.
For running conky after changes, pass the --run flag.

Example:<br>
**1. Pass the first element on settings.py path list (index 0)**
```sh
python3 conkyrc_updater.py 0
```
**2. Also running conky application:**
```sh
python3 conkyrc_updater.py 0 --run
```
