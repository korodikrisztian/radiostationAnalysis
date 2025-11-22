import csv
import os
import datetime

last_track = None

def create_csv(csv_filename):
    try:
        if not os.path.exists(csv_filename):
            with open(csv_filename, mode='w', newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(['datetime', 'title', 'duration'])
    except PermissionError:
        print('You do not have permission.')
    except OSError as e:
        print(f'File operation error {e}')

def write_to_csv(track, csv_filename):
    global last_track

    try:
        if last_track:
            duration = int((track['datetime'] - last_track['datetime']).total_seconds())

            with open(csv_filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            last_line = lines[-1].strip().split(',')
            last_line[2] = str(duration)
            lines[-1] = ','.join(last_line) + "\n"

            with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
                file.writelines(lines)

        with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([track['datetime'].strftime("%Y-%m-%d %H:%M:%S"), track['title'], 0])

        last_track = track

    except FileNotFoundError:
        print(f'File not found. {csv_filename}')
    except OSError as e:
        print(f'File operation error. {e}')
