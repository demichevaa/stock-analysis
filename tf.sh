#!/bin/bash

set -e  # Exit on error

ENV_FILE=".env"
TF_DIR="terraform"

if [[ -f "$ENV_FILE" ]]; then
    echo "Loading environment variables from $ENV_FILE:"

    while IFS='=' read -r key value; do
        if [[ -n "$key" && ! "$key" =~ ^# ]]; then
            export "TF_VAR_$key=$value"
            echo "  - $key"
        fi
    done < "$ENV_FILE"

    echo "Environment variables loaded successfully."
else
    echo "Warning: $ENV_FILE file not found - skipping."
fi

# Ensure Terraform directory exists before switching
if [[ -d "$TF_DIR" ]]; then
    cd "$TF_DIR"
else
    echo "Error: Terraform directory '$TF_DIR' not found."
    exit 1
fi

terraform "$@"
