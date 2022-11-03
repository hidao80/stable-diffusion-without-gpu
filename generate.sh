#!/bin/sh -ue

if [ -z "$1" ]; then
    echo "[Error] Prompt not found."
    exit 1;
fi

sudo docker-compose exec stable-diffusion /app/stable-diffusion/draw.py "$1"
