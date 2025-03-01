#!/bin/bash

set -e

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [INFO] $1"
}

log "Starting setup"

cd ./dtk_lib
log "Installing dtk_lib in editable mode"
pip install -e .

log "Creating symlink for dtk_lib as dtk"
ln -sf dtk_lib dtk


cd ../fin
log "Installing fin dependencies from requirements.txt"
pip install -r requirements.txt

log "Setup completed successfully."
