#!/bin/bash

file="./README.md"

# Get the last modification time of the file
last_modified=$(stat -f %m "$file")

# Store the current modification time in a variable
current_time=$(date +%s)

# Check if the file has been modified in the last minute
if [ "$((current_time - last_modified))" -le 1 ]; then
    echo "The file has been modified in the last minute."
else
    echo "The file has not been modified in the last minute."
fi