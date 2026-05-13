#!/bin/bash
echo "Файловая система     Использовано  Статус"
echo "-------------------  ------------  ------------"
df -h | awk 'NR>1 {
    filesystem = $1
    usage_percent = $5
    gsub(/%/, "", usage_percent)
if (usage_percent > 90) {
        status = "КРИТИЧНО!"
    } else {
        status = "OK"
    }
 printf "%-20s %-12s %s\n", filesystem, $5, status
}'
