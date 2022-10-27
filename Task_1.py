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

def people(list_doc):
    """people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит"""
    doc_command = input('Введите номер документа: ')
    for doc_list in list_doc:  # проходим по списку выделяя каждый словарь
        for v in doc_list.values():  # расспаковываем словарь для поиска по значению
            if v == doc_command:  # находим какому словарю принадлежит введенное значение номера документа
                return f'Имя: {doc_list["name"]}' # выводим имя человека из словаря, в соответствии с введенным номером документа
    else:
        return f"Документы с номером '{doc_command}' в списке отсутствуют" # выводим если документа с номером нет в списке


def shelf(list_shelf):
    """shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится"""
    doc_command = input('Введите номер документа: ')
    for k, v in list_shelf.items():  # расспаковываем словарь на ключ, значение
        if doc_command in v:  # проверяем условие наличия введенного номера в заначениях
            return f'Документ находится на полке №{k}'  # выводим номер полки
    else:
        return f"Документ с номером '{doc_command}' нет на полках"  # выводим если документа с номером нет в списке



def roster(doc):
    """roster – команда, которая выведет список всех документов """
    list_ = []
    for document in doc:
        doc_type =document['type']
        doc_number = document['number']
        doc_owner_name = document['name']
        l = f"{doc_type}, '{doc_number}', '{doc_owner_name}'"
        list_.append(l)
    return list_


def add_doc(list_doc, list_shelf):
    """add_doc – команда, которая добавит новый документ в каталог и в перечень полок,"""
    type_command = input('Введите тип документа: ')
    numb_command = input('Введите номер документа: ')
    name_command = input('Введите имя владельца: ').title()
    list_person = {'type': type_command, 'number': numb_command,
                   'name': name_command}  # создаем словарь из введенных значений
    list_doc.append(list_person)  # добавляет созданный словарь в список cловарей
    shelf_command = input('Введите номер полки хранения документа: ')
    if shelf_command in list_shelf:  # проверяем содержится введенный номер полки в имеющимся списке
        list_shelf[shelf_command].append(
            numb_command)  # если содержится, добавляем к имеющимуся списку новое значение по ключу
        return list_doc, list_shelf
    else:
        return f"Полка с номером '{shelf_command}' не существует."  # если полки с указанным номером не существует


def del_doc(list_doc, list_shelf):
    """del_doc – команда, которая спросит номер документа и удалит его из каталога и из перечня полок"""
    doc_command = input('Введите номер документа: ')
    for v in list_shelf.values():  # расспаковываем словарь на значение
        if doc_command in v:  # проверяем условие наличия введенного номера в заначениях
            v.remove(doc_command)  # если введенный номер есть в значениях удаляем его
            for id, doc_list in enumerate(list_doc):  # проходим по списку выделяя каждый словарь
                for v in doc_list.values():  # расспаковываем словарь для поиска по значению
                    if v == doc_command:  # находим какому словарю принадлежит введенное значение номера документа
                        list_doc.pop(id)  # удаляем словарь, содержащий введенный номер, из списка в соответствии с id
            return list_doc, list_shelf
    else:
        return f"Документ номер '{doc_command}' не существует."  # если указанного номера нет на полках


def move_shelf(list_shelf):
    """move_shelf – команда, которая спросит номер документа и целевую полку и переместит
    его с текущей полки на целевую"""
    doc_command = input('Введите номер документа: ')
    for v in list_shelf.values():  # расспаковываем словарь на значение
        if doc_command in v:  # проверяем условие наличия введенного номера в заначениях
            shelf_command = input('Введите номер полки для хранения документа: ')
            if shelf_command in list_shelf.keys():  # проверяем условие наличия номера полки
                v.remove(doc_command)  # удаляем номер документа с исходной полки
                list_shelf[shelf_command].append(doc_command)  # добавляем номер документа на заданную полку
                return list_shelf
            else:
                return f"Полка с номером '{shelf_command}' не существует."  # если полки с указанным номером не существует
    else:
        return f"Документ с номером '{doc_command}' не существует."  # если указанного номера нет на полках


def new_shelf(list_shelf):
    """new_shelf – команда, которая спросит номер новой полки и добавит ее в перечень"""
    shelf_command = input('Введите номер полки для хранения документа: ')
    if shelf_command not in list_shelf.keys():  # проверяем существует полка с указанным номером
        list_shelf[shelf_command] = []  # если не существует создаем новую с указанным номером
        return list_shelf
    else:
        return f"Полка с номером '{shelf_command}' существует."  # проверяет наличия существования полки с введеным номером


def main(list_doc, list_shelf):
    while True:
        command = input('Введите команду: ').lower()
        help_ = """ p – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
                    s – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
                    l – команда, которая выведет список всех документов;
                    a – команда, которая добавит новый документ в каталог и в перечень полок;
                    d – команда, которая удалит документ из каталога и из перечня полок;
                    m – команда, которая  переместит документ с текущей полки на целевую;
                    as – команда, которая добавит номер полки в ее перечень."""
        if command == 'p':
            print(people(documents))
        elif command == 's':
            print(shelf(directories))
        elif command == 'l':
            roster(documents)
        elif command == 'a':
            print(add_doc(documents, directories))
        elif command == 'd':
            print(del_doc(documents, directories))
        elif command == 'm':
            print(move_shelf(directories))
        elif command == 'as':
            print(new_shelf(directories))
        elif command == "help_":
            print(help_)
        elif command == 'exit':
            print('Выход')


if __name__ == '__main__':
    print(roster(documents))
    # print(main(documents, directories))
    # print(move_shelf(directories))
    # print(main(documents, directories))
#     print(add_doc(documents, directories))

