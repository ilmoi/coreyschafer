#!/bin/sh

cd "/Users/ilja/Dropbox/atbs"

a=(a b c d)
a[5]=f
a+=(e f g)
echo ${a[@]}
echo ${a[2]}

for i in ${a[@]}; do
    echo $i
done

echo -----

echo ${#a[@]}
unset a[2]
echo ${a[@]}
unset $a
echo ${a[@]}
