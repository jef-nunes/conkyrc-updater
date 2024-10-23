# Path utils
from os import path
# Proccess spawning
from subprocess import Popen
# Custom settings
from settings import config_files, conkyrc_path, conkyrc_backup_path 
# CLI args
import argparse
# Copying files
import shutil
# Exit codes
import sys

# Must import the content of ./settings.py
# Which includes a list containing the paths
# to the configuration files custom .conkyrc files
# Example:
# config_files = [
#    "/home/myuser/Scripts/conkyrc_v1.lua",
#    "/home/myuser/Scripts/conkyrc_v2.lua"
# ]

def set_conkyrc(index, run_conky):
    if index>=0 and index < len(config_files):
        # Make a backup of the current file
        shutil.copyfile(conkyrc_path, conkyrc_backup_path)

        # Read the new configuration file
        with open(config_files[index], 'r') as source_file:
            new_content = source_file.read()
        
        # Write the new content to the .conkyrc file
        with open(conkyrc_path, 'w') as dest_file:
            dest_file.write(new_content)
        
        print("Success: ~/.conkyrc updated.")

        # Run conky if the --run flag is passed
        if run_conky:
            conky_proc = Popen(["conky"])
            print("Running conky...")
            input("Press [Return] to quit program...")
            conky_proc.terminate()
    else:
        print("Error - Invalid configuration file index.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update .conkyrc configuration")
    parser.add_argument("index", type=int, help="Index of the configuration file")
    parser.add_argument("--run", action="store_true", help="Run conky after updating")
    args = parser.parse_args()
    
    set_conkyrc(args.index, args.run)

