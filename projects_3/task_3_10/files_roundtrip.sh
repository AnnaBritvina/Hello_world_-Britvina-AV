#!/bin/bash
echo "=== Создание файлов==="

for i in 1 2 3 4 5 6 7 8 9 10
do
    filename="test${i}.txt"
    touch "$filename"
    echo "Создан файл: $filename"
done
echo -e "\n=== Удаление файлов в обратном порядке с помощью while ==="

i=10
while [ $i -ge 1 ]
do
    rm "test${i}.txt"
    echo "Удален: test${i}.txt"
    i=$((i - 1))
done
