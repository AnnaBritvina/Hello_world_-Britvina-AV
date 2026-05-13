#!/bin/bash
i=1
while [ $i -le 20 ]
do
    if [ $((i % 2)) -eq 0 ]; then
        i=$((i+1))
        continue
    fi
if [ $i -eq 15 ]; then
        break
    fi
echo $i
    i=$((i+1))
done
