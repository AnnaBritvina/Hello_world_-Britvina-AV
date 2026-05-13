#!/bin/bash
echo "Введите имя гена:"
read gene
echo "Введите уровень экспрессии гена:"
read expression
if [ -z "$gene" ] || [ -z "$expression" ]; then
    echo "Ошибка: имя гена и уровень экспрессии должны быть введены"
    exit 1
fi
echo "Экспрессия гена $gene составляет $expression единиц"
