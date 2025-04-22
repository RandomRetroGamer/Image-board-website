#!/bin/bash
clear


echo " --- starting build --- "
echo " "

source startup.sh
echo " --- starting local enviroment --- "
echo "! linux start build ! "
echo " "
echo " "

python3 main.py

deactivate


echo " !enviroment stoped! "
echo " "
echo " --- build successful --- "
