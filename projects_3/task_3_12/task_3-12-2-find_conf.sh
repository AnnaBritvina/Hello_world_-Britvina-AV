#!/bin/bash
echo "=== Поиск файлов с расширением .conf (или .CONF) в директории /etc ==="
echo ""
ls -l /etc | grep -i "\.conf"
