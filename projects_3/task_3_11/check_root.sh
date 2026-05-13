#!/bin/bash
show_message() {
    local TYPE=$1
    local MESSAGE=$2
    local DATE=$(date +"%H:%M:%S")
    echo "[$DATE] [$TYPE]: $MESSAGE"
}
check_root() {
    if [ $EUID -ne 0 ]; then
        echo "ОШИБКА: Скрипт должен быть запущен от имени суперпользователя (root)!"
        echo "Используйте: sudo $0"
        exit 1
    fi
}
check_root
echo "Скрипт запущен от имени root. Продолжаем выполнение..."
