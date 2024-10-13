#!/bin/bash

export km_execute=0
export km_walk_image=0
export km_script='script'
export km_path_script="/Users/leolau/Documents/CODE/km/auto/$km_script"
export km_path_report="$km_path_script/report"

flag_s=false
action_s="check syntax find.py, walk_image.py"
flag_p=false
action_p="plan by find.py, walk_image.py"
flag_e=false
action_e="execute by walk_image.py"



help="
Usage: 
[-s]  $action_s
[-p]  $action_p
[-e]  $action_e
"

while getopts "spe" option; do
    case $option in
        s) flag_s=true ;;
        p) flag_p=true ;;
        e) flag_e=true ;;
        *) echo "$help" ;;
    esac
done

if [ "$#" -eq 0 ]; then
    echo "$help"
fi

if [  "$1" = "-" ]; then
    echo "$help"
fi

if [ "$flag_s" = true ]; then
    km_execute=0
    echo $action_s

    echo $action_p
    python -m "$km_script.run" | tee "$km_path_report/walk_image_syntax.txt"
    echo "output saved to $km_path_report/walk_image_syntax.txt"

fi

if [ "$flag_p" = true ]; then
    km_execute=0
    km_walk_image=1
    echo $action_s

    echo $action_p
    python -m "$km_script.run" | tee "$km_path_report/walk_image.txt"
    echo "output saved to $km_path_report/walk_image.txt"
    echo "set -e to $action_e"
    
    
fi

if [ "$flag_e" = true ]; then
    echo $action_e
    km_execute=1
    km_walk_image=1
    python -m "$km_script.run" | tee "$km_path_report/walk_image.txt"
fi


