#!/bin/bash

pgrep waybar > /dev/null && 
  killall waybar ||
    waybar -c $HOME/.config/waybar/top_bar/config -s $HOME/.config/waybar/top_bar/style.css & > /dev/null
