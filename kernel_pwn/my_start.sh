#!/bin/sh

gcc ./exp.c -static -lpthread -o exp
#gcc ./exp.c -static -lpthread -o exp
cp exp ./cpio
cd cpio
./gen.sh #need name here
cd ..
./startvm.sh