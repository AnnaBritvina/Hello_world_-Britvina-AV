#!/bin/bash
echo "=== Замена пути к базе данных в settings.php ==="
echo ""
sed -i 's|/var/lib/mysql/data|/mnt/ssd/mysql|g'
echo "Путь к БД успешно изменен в settings.php"

