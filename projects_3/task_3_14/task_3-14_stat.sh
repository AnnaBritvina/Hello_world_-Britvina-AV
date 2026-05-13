#!/bin/bash
echo "Сумма: $(awk '{sum+=$2} END {print sum}' students.txt)"
echo "Среднее: $(awk '{sum+=$2} END {printf "%.2f", sum/NR}' students.txt)"
echo "Максимум: $(awk 'NR==1{max=$2} $2>max{max=$2} END {print max}' students.txt)"
