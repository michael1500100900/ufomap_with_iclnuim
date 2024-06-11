#!/bin/bash

# Ścieżka do katalogu z plikami .bt
BT_DIRECTORY="office_room"

# Uruchomienie roscore, jeśli nie jest już uruchomiony
if ! pgrep -x "roscore" > /dev/null
then
    roscore &
    sleep 5
fi

# Uruchomienie octomap_server dla każdego pliku .bt
for bt_file in "$BT_DIRECTORY"/*.bt
do
    echo "Ładowanie pliku $bt_file do OctoMap..."
    rosrun octomap_server octomap_server_node _filename:=$bt_file
    sleep 2
done
