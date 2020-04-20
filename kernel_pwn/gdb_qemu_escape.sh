#!/bin/bash
find_pid(){
    pid_addr=$1
}
res=`ps -A|grep vim`

echo "[+] get the ps message"

find_pid $res
echo "[+] get pid" 
echo $pid_addr
echo "[+] lanuch gdb"

sudo gdb \
    -ex "attach $pid_addr" \
    -ex "handle SIGINT nostop" \
    -ex "set follow-fork-mode parent" \
    -ex "b *(0x555555554000+0x029AF83)"