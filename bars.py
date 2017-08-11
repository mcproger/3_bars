from math import sqrt
import json, os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='cp1251') as file_handler:
        return json.load(file_handler)


def make_bars_seats_place_info(data):
    bars_seats_place_info = {}
    for bar in bars:
        bars_seats_place_info[bar.get('Name', None)] = bar.get('SeatsCount', None)
    return bars_seats_place_info


def make_bars_coordinates_info(data, longitude, latitude):
    bars_coordinates_info = {}
    for bar in bars:
        width = (longitude - float(bar.get('Longitude_WGS84', 0))) ** 2
        length = (latitude - float(bar.get('Latitude_WGS84', 0))) ** 2
        bars_coordinates_info[bar.get('Name', None)] = sqrt(width + length)
    return bars_coordinates_info


def get_biggest_bar(data):
    bars_seats_place_info = make_bars_seats_place_info(data)
    biggest_bar = max(bars_seats_place_info.items(), key=lambda item: item[1])[0]
    return biggest_bar


def get_smallest_bar(data):
    bars_seats_place_info = make_bars_seats_place_info(data)
    smallest_bar = min(bars_seats_place_info.items(), key=lambda item: item[1])[0]
    return smallest_bar


def get_closest_bar(data, longitude, latitude):
    bars_coordinates_info = make_bars_coordinates_info(data, longitude, latitude)
    closest_bar = min(bars_coordinates_info.items(), key=lambda item: item[1])[0]
    return closest_bar


if __name__ == '__main__':
    filepath = input('Введите путь до файла с барами: ')
    longitude = float(input('Введите долготу: '))
    latitude = float(input('Введите широту: '))
    if load_data(filepath):
        bars = load_data(filepath)
        print('Самый большой бар -', get_biggest_bar(bars))
        print('Самый маленький бар -', get_smallest_bar(bars))
        print('Самый близкий бар -', get_closest_bar(bars, longitude, latitude))
    else:
        print('Такого файла нет')