from bs4 import BeautifulSoup
from colorama import Fore
from pprint import pprint
import requests
import random
import time
import lxml
import csv
import sys
import os
import re


def get_source(params=None, models=None):
    headers = {
        'authority': 'www.polovniautomobili.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9,sr;q=0.8,hy;q=0.7,bs;q=0.6',
    }

    if models:
        headers = {
            'authority': 'www.polovniautomobili.com',
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.polovniautomobili.com/',
            'accept-language': 'en-US,en;q=0.9,sr;q=0.8,hy;q=0.7,bs;q=0.6',
        }

    try:
        if params and not models:
            url = 'https://www.polovniautomobili.com/search/models'
            r = requests.get(url, headers=headers, params=params, timeout=10)
        elif params and models:
            url = 'https://www.polovniautomobili.com/auto-oglasi/pretraga'
            r = requests.get(url, headers=headers, params=params, timeout=10)
        elif not params and not models:
            url = 'https://www.polovniautomobili.com/'
            r = requests.get(url, headers=headers, timeout=10)

        time.sleep(r.elapsed.total_seconds())
        status_code = r.status_code
        if status_code == 200:
            return BeautifulSoup(r.text, 'lxml')
        else:
            print('Status code: ', status_code)
            return
    except:
        print('ERROR')
        return


def extract_data():
    soup = get_source()
    if not soup:
        return None

    counter = 0
    # All brands
    all_brands = soup.select('#brand > option')
    if all_brands:
        for brand in all_brands[1:-1]:
            brand_ = brand.get('value')
            params = (
                ('category', '26'),
                ('brand', brand_),
                ('type', 'full'),
                ('names', 'true'),
            )
            soup = get_source(params=params)
            if not soup:
                return None

            # All models
            all_models = soup.select('option')

            if all_models:
                for model in all_models[0:-1]:
                    model_ = model.get('value')
                    params = (
                        ('brand', brand_),
                        ('model[]', model_),
                        ('price_to', ''),
                        ('year_from', ''),
                        ('year_to', ''),
                        ('showOldNew', 'all'),
                        ('submit_1', ''),
                        ('without_price', '1'),
                    )

                    soup = get_source(params=params, models=True)
                    if not soup:
                        return None

                    # Total amount of vehicles
                    total_vehicles = soup.select_one('div.js-hide-on-filter > small')
                    total_vehicles = total_vehicles.get_text(strip=True).split()[-1] if total_vehicles else ''

                    csv_writer.writerow([brand_, model_, total_vehicles])

                    counter += 1
                    print(f'{counter}. Brand: {brand_}, Model: {model_}, Total Vehicles: {total_vehicles}')


def save_data():

    file_name = 'data/used_cars_data.csv'
    file_exists = os.path.exists(file_name)
    with open(file_name, 'a', newline='', errors='ignore', encoding='utf-8') as f:
        global csv_writer
        csv_writer = csv.writer(f)

        if not file_exists:
            csv_writer.writerow(['Brand', 'Model', 'Total Vehicles'])

        extract_data()


############################
# Running the script
save_data()
############################









