#!/bin/bash
echo "Студенты с оценкой ВЫШЕ 80:"
awk '$2 > 80' students.txt
echo "Студенты с оценкой НИЖЕ 70:"
awk '$2 < 70' students.txt
echo "Первая строка файла:"
awk 'NR==1' students.txt
