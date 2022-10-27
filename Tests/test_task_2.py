from Task_2 import new_folder, full_path
import pytest
import requests

params_ = ['test', 123,'Лок', False, "?????*^&&*", " "]


@pytest.fixture(params=params_)
def tear_down():
    yield
    with open(full_path) as file_object:
        TOKEN_YD = file_object.readline().strip()
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {'Content-Type': 'application/json',
               'Authorization': f'OAuth {TOKEN_YD}'
               }
    param = {'path': params_}
    response = requests.delete(upload_url, headers=headers, params=param)
    return response.status_code


def test_new_folder_good(tear_down):
    assert new_folder(params_) == 201


@pytest.mark.parametrize("name", [None, ""])
def test_new_folder_error_1(name):
    assert new_folder(name) == 400
