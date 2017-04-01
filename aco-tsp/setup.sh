#!/bin/bash

if ! type "pip3.5" > /dev/null; then
  echo "Please install pip3.5"
else
 pip3.5 install numpy matplotlib pants --user
fi

