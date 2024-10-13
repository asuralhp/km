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