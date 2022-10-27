from copy import deepcopy
import pytest
import mock

from Task_1 import people, shelf, del_doc, new_shelf, roster, add_doc, move_shelf

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

doc_copy = documents.copy()
dir_copy = deepcopy(directories)
dir_copy_1 = deepcopy(directories)
dir_copy_2 = deepcopy(directories)

document_list = ["passport, '2207 876234', 'Василий Гупкин'",
                 "invoice, '11-2', 'Геннадий Покемонов'",
                 "insurance, '10006', 'Аристарх Павлов'"]

documents_new = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "passport", "number": "777", "name": "Иван Соколов"}
]

directories_new = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': ['777']
}

documents_new_2 = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories_new_2 = {
    '1': ['2207 876234', '5455 028765'],
    '2': ['10006'],
    '3': []
}

directories_new_3 = {
    '1': ['11-2', '5455 028765'],
    '2': ['10006'],
    '3': ['2207 876234']
}

directories_new_4 = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': [],
    '4': []
}


@pytest.mark.parametrize('doc_, numb, result', [(documents, '10006', 'Имя: Аристарх Павлов'),
                                               (documents, '2207 876234', 'Имя: Василий Гупкин'),
                                               (documents, '1000', "Документы с номером '1000' в списке отсутствуют")
                                               ])
def test_people(doc_, numb, result):
    with mock.patch('builtins.input', return_value=numb):
        assert people(doc_) == result


@pytest.mark.parametrize('dir_, numb, result', [(directories, '10006', 'Документ находится на полке №2'),
                                                (directories, '11-2', 'Документ находится на полке №1'),
                                                (directories, '106', "Документ с номером '106' нет на полках")
                                                ])
def test_shelf(dir_, numb, result):
    with mock.patch('builtins.input', return_value=numb):
        assert shelf(dir_) == result


@pytest.mark.parametrize('doc_, result', [(documents, document_list)])
def test_roster(doc_, result):
    assert roster(doc_) == result


def test_add_doc():
    with mock.patch('builtins.input', side_effect=['passport', '777', 'Иван Соколов', '3']):
        assert add_doc(documents, directories) == (documents_new, directories_new)


def test_del_doc():
    with mock.patch('builtins.input', return_value='11-2'):
        assert del_doc(doc_copy, dir_copy) == (documents_new_2, directories_new_2)


@pytest.mark.parametrize('dir_, result, number_doc, number_shelf',
                         [(dir_copy_1, directories_new_3, "2207 876234", "3"),
                          (dir_copy_1, "Полка с номером '5' не существует.", "2207 876234", "5"),
                          (dir_copy_1, "Документ с номером '777777' не существует.", "777777", "5")
                          ])
def test_move_shelf(dir_, result, number_doc, number_shelf):
    with mock.patch('builtins.input', side_effect=[number_doc, number_shelf]):
        assert move_shelf(dir_) == result


@pytest.mark.parametrize('dir_, result, number_shelf',
                        [(dir_copy_2, directories_new_4, "4"),
                         (dir_copy_2, "Полка с номером '1' существует.", "1")
                         ])
def test_new_shelf(dir_, result, number_shelf):
    with mock.patch('builtins.input', return_value=number_shelf):
        assert new_shelf(dir_) == result


def test_add_doc_exceptions():
    with mock.patch('builtins.input', side_effect= ['passport', '777', 'Иван Соколов', '7']):
        assert add_doc(documents, directories) == "Полка с номером '7' не существует."


def test_del_doc_exceptions():
    with mock.patch('builtins.input', return_value='11111-2'):
        assert del_doc(doc_copy, dir_copy) == "Документ номер '11111-2' не существует."



