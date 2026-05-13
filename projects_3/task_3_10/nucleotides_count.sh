#!/bin/bash
printf "%-15s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"
for file in *.fasta
do [ -f "$file" ] || continue
if [ ! -s "$file" ]; then
        continue
    fi
sequence=$(grep -v "^>" "$file" | tr -d '\n')
count_A=$(echo "$sequence" | grep -o "[Aa]" | wc -l)
count_T=$(echo "$sequence" | grep -o "[Tt]" | wc -l)
count_G=$(echo "$sequence" | grep -o "[Gg]" | wc -l)
count_C=$(echo "$sequence" | grep -o "[Cc]" | wc -l)
printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$count_A" "$count_T" "$count_G" "$count_C"
done
