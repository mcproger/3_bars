from math import sqrt
import json, os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='cp1251') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    bars_info = {}
    for bar in bars:
    	bars_info[bar.get('Name', None)] = bar.get('SeatsCount', None)
    biggest_bar = max(bars_info.items(), key=lambda item: item[1])[0]
    return biggest_bar


def get_smallest_bar(data):
    bars_info = {}
    for bar in bars:
    	bars_info[bar.get('Name', None)] = bar.get('SeatsCount', None)
    smallest_bar = min(bars_info.items(), key=lambda item: item[1])[0]
    return smallest_bar


def get_closest_bar(data, longitude, latitude):
    bars_info = {}
    for bar in bars:
        width = (float(longitude) - float(bar.get('Longitude_WGS84', 0))) ** 2
        length = (float(latitude) - float(bar.get('Latitude_WGS84', 0))) ** 2
        bars_info[bar.get('Name', None)] = sqrt(width + length)   
    closest_bar = min(bars_info.items(), key=lambda item: item[1])[0]
    return closest_bar


if __name__ == '__main__':
    filepath = input('Введите путь до файла с барами: ')
    longitude = input('Введите долготу: ')
    latitude = input('Введите широту: ')
    bars = load_data(filepath)
    print('Самый большой бар -', get_biggest_bar(bars))
    print('Самый маленький бар -', get_smallest_bar(bars))
    print('Самый близкий бар -', get_closest_bar(bars, longitude, latitude))
