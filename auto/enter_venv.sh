
current_dir=$(basename "$(pwd)")

if [ "$current_dir" = "script" ]; then
    source ./.venv/bin/activate
else
    cd ./script
    source ./.venv/bin/activate
    cd ..
fi
