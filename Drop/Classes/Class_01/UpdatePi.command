#!/bin/bash

# UpdatePi.command
# Desc : This command is used to update your Raspberry Pi 
# Vers : 1.0.0
# Date : 06/15/2018
# Auth : Andrew Tyler Pierce (typhoontong22)

################################################################
# DO NOT USE THIS COMMAND IF YOU DO NOT HAVE ENOUGH DISK SPACE #
################################################################

sudo apt-get update

printf 'y\n' | sudo apt-get dist-upgrade

sudo apt-get update

sudo apt-get clean