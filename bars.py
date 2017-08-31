from math import sqrt
import json
import os
import argparse


def get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str,
                        help='Path to file with bar\'s list')
    parser.add_argument('longitude', type=float)
    parser.add_argument('latitude', type=float)
    args = parser.parse_args()
    return args


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='cp1251') as file_handler:
        return json.load(file_handler)


def get_bar_name(bar_info):
    bar_name = bar_info['Name']
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
    return min(bars, key=lambda bars: get_distance_to_bar(bars, longitude, latitude))


if __name__ == '__main__':
    args = get_argparser()
    bars = load_data(args.filepath)
    if not bars:
        print('Такого файла нет')
    else:    
        print('Самый большой бар -', get_bar_name(get_biggest_bar(bars)))
        print('Самый маленький бар -', get_bar_name(get_smallest_bar(bars)))
        print('Самый близкий бар -',
              get_bar_name(get_closest_bar(bars, args.longitude, args.latitude)))
