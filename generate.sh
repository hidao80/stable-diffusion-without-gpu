#!/bin/sh -ue

if [ -z "$1" ]; then
    echo 'Usage: generate.sh "prompt" ["image.png"]'
    exit 1;
fi

now=$(date '+%Y%m%d_%T' | tr -d :)
if [ $# -eq 1 ]; then
    docker-compose exec stable-diffusion /app/stable-diffusion/draw.py $now "$1"
elif [ $# -eq 2 ]; then
    # Copy the teacher image into the container
    docker-compose cp "$2" stable-diffusion:/app    
    docker-compose exec stable-diffusion /app/stable-diffusion/draw.py $now "$1" /app/$(basename "$2")
else
    echo 'Usage: generate.sh prompt [image.png]'
fi
