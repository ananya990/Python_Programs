# Import the Path class from the pathlib module
from pathlib import Path

# Create a Path object representing the directory path "/root/dirA/dirB"
# This doesn't actually create the directory, it just represents the path
directory_path = Path("/root/dirA/dirB")

# Use the mkdir() method to create the directory represented by directory_path
# parents=True creates parent directories if they don't exist
# exist_ok=True avoids raising an exception if the directory already exists
directory_path.mkdir(parents=True, exist_ok=True)
