#!/bin/sh

cd ./source/tools/MyPinTool/
make obj-intel64/itrace.so TARGET=intel64
cp obj-intel64/itrace.so ~/ctf/pin-3.7/
cd ~/ctf/pin-3.7/
./pin -t itrace.so -- ./my_bin/easyparser #change bin name here
cat itrace.out