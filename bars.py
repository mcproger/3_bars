from math import sqrt
import json, os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='cp1251') as file_handler:
        return json.load(file_handler)


def get_bar_name(bar_info):
    bar_name = bar_info['Name']
    bar_address = bar_info['Address']
    return bar_name


def get_distance_to_bar(bars, longitude, latitude):
    bar_longtitude = (longitude - float(bars['Longitude_WGS84'])) ** 2
    bar_latitude = (latitude - float(bars['Latitude_WGS84'])) ** 2
    return sqrt(bar_longtitude + bar_latitude)


def get_biggest_bar(bars):
    return max(bars, key=lambda bars: bars['SeatsCount'])


def get_smallest_bar(bars):
    return min(bars, key=lambda bars: bars['SeatsCount'])


def get_closest_bar(bars, longitude, latitude):
    return min(bars, key=lambda bars: get_distance(bars, longitude, latitude))


if __name__ == '__main__':
    filepath = input('Введите путь до файла с барами: ')
    longitude = float(input('Введите долготу: '))
    latitude = float(input('Введите широту: '))
    if load_data(filepath):
        bars = load_data(filepath)
        print('Самый большой бар -', get_bar_name(get_biggest_bar(bars)))
        print('Самый маленький бар -', get_bar_name(get_smallest_bar(bars)))
        print('Самый близкий бар -', get_bar_name(get_closest_bar(bars, longitude, latitude)))
    else:
        print('Такого файла нет')