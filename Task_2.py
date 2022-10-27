import requests
import os

FILE_TOKEN = "token.txt"
PATH_FILE_TOKEN = os.path.dirname(os.path.abspath(__file__))
full_path = os.path.join(PATH_FILE_TOKEN, FILE_TOKEN)


with open(full_path) as file_object:
    TOKEN_YD = file_object.readline().strip()


def new_folder(name):
    """Создаем новую папку"""
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {'Content-Type': 'application/json',
               'Authorization': f'OAuth {TOKEN_YD}'
               }
    params = {'path': name}
    response = requests.put(upload_url, headers=headers, params=params)
    return response.status_code


if __name__ == '__main__':
    print(new_folder('Test'))

