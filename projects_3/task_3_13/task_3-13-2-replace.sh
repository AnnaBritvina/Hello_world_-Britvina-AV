#!/bin/bash
sed -i 's/ /\t/g' sequences.txt
echo -e "\nРезультат (табуляция показана как ^I):"
cat -A sequences.txt
