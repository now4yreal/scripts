#!/bin/sh
gdb \
    -ex "file vmlinux" \
    -ex 'set follow-mode parent' \
    -ex 'set arch i386:x86-64:intel' \
    -ex 'target remote localhost:1234' \
    -ex 'add-symbol-file noob.ko 0xffffffffc0002000' \
    -ex 'b *0xffffffffc0002000+0x421' \
    -ex 'b *0xffffffffc0002000+0x16b' \
    -ex 'b *0xffffffffc0002000+0xcc' \
    -ex 'c' 
