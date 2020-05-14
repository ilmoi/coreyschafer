#!/bin/sh

cd "/Users/ilja/Dropbox/atbs"

a=1020304050
r="^[0-9]{8,}$"

if [[ $a =~ $r ]]; then
    echo yassss
fi
