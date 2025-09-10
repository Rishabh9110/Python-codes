import os

# Specify the directory you want to list
directory = '/'  # Current directory

try:
    # List all files and directories in the specified path
    contents = os.listdir(directory)
    
    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory}' was not found.")
except PermissionError:
    print(f"Permission denied to access '{directory}'.")
