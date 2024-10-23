# Used to resolve user home path
from os.path import expanduser

conkyrc_backup_path = expanduser("~/.conkyrc.bak")
conkyrc_path = expanduser("~/.conkyrc")
config_files = [
    # Insert the custom .conkyrc files paths here
]
