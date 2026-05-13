#!/bin/bash
echo "Введите массу тела (в кг):"
read weight
echo "Введите рост (в метрах):"
read height
bmi=$(echo "scale=2; $weight / ($height * $height)" | bc)
echo "Ваш индекс массы тела (ИМТ): $bmi"
