import os
import csv

DATA_HEADERS = ['ID','Nazwa', 'Link', 'Opis', 'Tagi', 'Polubienia']
DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'

def get_whole_table():
    result = []
    with open(DATA_FILE_PATH, 'r') as file:
        for line in file.readlines():
            result.append(line.strip().split(';'))
    return result
