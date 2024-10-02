#!/bin/bash
# Written by lr2t9iz (2023.11.01)

# rotate active container logs

container_names=($(docker ps --format "{{.Names}}"))
N0W=$(date +%Y.%m.%d)

for name in "${container_names[@]}"; do
  cp $(docker inspect --format='{{.LogPath}}' $name) ./$N0W-$name.log
  echo "" > $(docker inspect --format='{{.LogPath}}' $name)
done
