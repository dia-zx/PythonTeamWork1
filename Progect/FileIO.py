# Модуль взаимодействия с файловой системой

# функция записи базы данных в файл
# dic - словарь записей баз данных dic ~ {ID : [Surname, Name, MiddleName, BirthDay, EMail, Telephone, Job, Note]}
from create_user import create_user


def save():
    with open('base', 'a', encoding='utf-8') as f:
        f.write(create_user())

    return 'All right'

# функция загрузки базы данных из файла
def load():
    with open('base', 'r', encoding='utf-8') as f:
        load_base = f.read()
    return load_base


save()
print(load())


# diction = {1: ['surname', 'name', 'middlename', 'birthday', 'email', 'telephone', 'job', 'note']}
# load(diction)
# print(load(*diction[1]))

