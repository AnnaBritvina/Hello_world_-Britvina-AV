#!/bin/bash
echo "Задание 1: Только имена"
awk '{print $1}' students.txt
echo "Задание 2: Только оценки"
awk '{print $2}' students.txt
echo "Задание 3: Номер строки и имя"
cat -n students.txt | awk '{print "Строка " $1 ": " $2}'
