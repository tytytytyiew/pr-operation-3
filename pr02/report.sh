#!/usr/bin/env bash
# Скрипт для анализа логов (Вариант B) - Барысбек

set -euo pipefail

show_help() {
    echo "Использование: $0 <папка_с_логами> <уровень> [--top N]"
    exit 1
}

if [ $# -lt 2 ]; then
    show_help
fi

target_dir="$1"
log_level="$2"
limit=0

if [ ! -d "$target_dir" ]; then
    echo "Ошибка: директория '$target_dir' не найдена!" >&2
    exit 1
fi

if [ $# -ge 4 ] && [ "$3" == "--top" ]; then
    limit="$4"
fi

if [ "$limit" -gt 0 ]; then
    grep -h "$log_level" "$target_dir"/*.log 2>/dev/null | awk -F'module=' '{print $2}' | awk '{print $1}' | sort | uniq -c | sort -nr | head -n "$limit" | awk '{printf "%-15s %s\n", $2, $1}'
else
    grep -h "$log_level" "$target_dir"/*.log 2>/dev/null | awk -F'module=' '{print $2}' | awk '{print $1}' | sort | uniq -c | sort -nr | awk '{printf "%-15s %s\n", $2, $1}'
fi
