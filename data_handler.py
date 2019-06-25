import os
import csv

DATA_HEADERS = ['ID','Nazwa', 'Link', 'Opis', 'Tagi', 'Polubienia']
DATA_TO_LOAD_FROM_USER = ['Nazwa', 'Link', 'Opis', 'Tagi']
DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'

def get_whole_table():
    result = []
    with open(DATA_FILE_PATH, 'r') as file:
        for line in file.readlines():
            result.append(line.strip().split(';'))
    return result

def add_data_to_file(data):
    with open(DATA_FILE_PATH, 'a') as file:
        file.write('\n')
        for item in data:
            file.write(item)
            file.write(';')
