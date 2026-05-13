#!/bin/bash
if [ ! -f sequences.txt ]; then
    echo "Ошибка: файл sequences.txt не найден!"
    echo "Сначала создайте его."
    exit 1
fi
echo "Замена пробелов на табуляцию в sequences.txt..."
sed -i 's/ /\t/g' sequences.txt
echo "Готово!"
echo -e "\nРезультат (табуляция показана как ^I):"
cat -A sequences.txt
