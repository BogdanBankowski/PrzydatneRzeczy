import os
import fileinput

DATA_HEADERS = ['ID','Nazwa', 'Link', 'Opis', 'Tagi', 'Polubienia']
DATA_TO_LOAD_FROM_USER = ['Nazwa', 'Link', 'Opis', 'Tagi']
DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
LIKES_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'likes.csv'
def get_whole_table(path):
    result = []
    with open(path, 'r') as file:
        for line in file.readlines():
            result.append(line.split(';'))
    return result

def add_data_to_file(data):
    with open(DATA_FILE_PATH, 'a') as file:
        file.write('\n')
        i=0
        for item in data:
            file.write(item)
            if i != len(data)-1:
                file.write(';')
            i += 1            #Taka logika zeby nie dodawal ';' na koncu linijki bo dodawalo to pusty wyraz do tabeli

def raise_likes_quantity_by_one(post_id):
    with open(LIKES_FILE_PATH, 'r') as file:
        post_id = post_id[1:-1]
        likes_dict = {}
        for line in file.readlines():
            line_as_list = line.split(';')
            likes_dict[line_as_list[0]] = int(line_as_list[1])
        likes_dict[post_id] += 1
        overwrite_likes_file(likes_dict)

def overwrite_likes_file(likes_dict):
    with open(LIKES_FILE_PATH, 'w') as file:
        for key in likes_dict.keys():
            file.write(key+';'+str(likes_dict[key])+'\n')

def get_whole_dictionary(path):
    result = {}
    with open(path, 'r') as file:
        for line in file.readlines():
            temp_line = line.split(';')
            temp_line[1] = temp_line[1].rstrip('\n')
            result[temp_line[0]] = temp_line[1]
    return result





