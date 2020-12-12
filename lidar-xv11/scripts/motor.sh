#!/bin/bash
state=$((1 - $(cat /sys/class/gpio/gpio388/value)))
if [ ! -z ${1} ]; then
    if [ ${1} = "on" ]; then
        state=1
    fi
    if [ ${1} = "off" ]; then
        state=0
    fi
fi
echo ${state} > /sys/class/gpio/gpio388/value