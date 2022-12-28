#!/bin/bash

pgrep waybar > /dev/null && 
  killall waybar ||
    waybar & > /dev/null
