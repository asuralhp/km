#!/bin/bash

# Initialize variables
FOLDER_NAME=""
PARENT_PATH=""

# Parse command-line options
while getopts "n:p:" opt; do
    case $opt in
        n) FOLDER_NAME="$OPTARG" ;;
        p) PARENT_PATH="$OPTARG" ;;
        *) echo "Usage: $0 -n <folder_name> -p <parent_path>" && exit 1 ;;
    esac
done

# Check if both parameters are provided
if [ -z "$FOLDER_NAME" ] || [ -z "$PARENT_PATH" ]; then
    echo "Usage: $0 -n <folder_name> -p <parent_path>"
    exit 1
fi

# Get the current script path
SCRIPT_PATH="$(dirname "$(realpath "$0")")"

# Create the new folder with the specified name at the specified path
NEW_FOLDER="$PARENT_PATH/$FOLDER_NAME"
mkdir -p "$NEW_FOLDER"

# Create a static folder inside the new folder
STATIC_FOLDER="$NEW_FOLDER/static"
mkdir -p "$STATIC_FOLDER"

# Create a new README.md file with the folder name as a header
README_FILE="$NEW_FOLDER/README.md"
echo "# $FOLDER_NAME" > "$README_FILE"

# Print the paths
echo "Created folder: $NEW_FOLDER"
echo "Created static folder: $STATIC_FOLDER"
echo "Created README.md: $README_FILE"