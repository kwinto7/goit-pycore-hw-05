import sys
from collections import defaultdict


def parse_log_line(line: str) -> dict:
    line_parts = line.strip().split(maxsplit=3)
    if len(line_parts) < 4:
        return {}
    return {
        'timestamp': f'{line_parts[0]} {line_parts[1]}',
        'level': line_parts[2],
        'message': line_parts[3]
    }

def load_logs(file_path) -> list:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [parse_log_line(line) for line in file if parse_log_line(line)]
    except FileNotFoundError:
        print(f'Файл {file_path} не знайдено.')
        return []
    except Exception as e:
        print(f'Помилка при читанні файлу: {e}')
        return []

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].lower() == level.lower()]

def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] +=1
    return dict(counts)

def display_log_counts(counts: dict):
    print(f"\n{'Рівень логування':<10} | {'Кількість':<5}")
    print("-" * 28)
    for level in sorted(counts.keys()):
        print(f"{level:<16} | {counts[level]:<5}")


def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до лог-файлу як аргумент.")
        return
    
    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)
    
    if not logs:
        print("Файл порожній або має неправильний формат.")
        return

    if len(sys.argv) >= 3:
        level_filter = sys.argv[2]
        filtered = filter_logs_by_level(logs, level_filter)
        print(f"\nЗаписи рівня '{level_filter.upper()}':")
        for log in filtered:
            print(f"{log['timestamp']} {log['level']} {log['message']}")
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
        
    
if __name__ == "__main__":        
    main()