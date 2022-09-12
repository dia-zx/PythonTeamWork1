# Модуль взаимодействия с файловой системой

# функция записи базы данных в файл
# dic - словарь записей баз данных dic ~ {ID : [Surname, Name, MiddleName, BirthDay, EMail, Telephone, Job, Note]}

import create_user

def save():
    with open('base', 'a', encoding='utf-8') as f:
        f.write(create_user.create_user())
    return create_user.create_user()


# функция загрузки базы данных из файла
def load():
    with open('base', 'r', encoding='utf-8') as f:
        load_base = f.read()
    return load_base


print(save())
print(load())

# diction = {1: ['surname', 'name', 'middlename', 'birthday', 'email', 'telephone', 'job', 'note']}
# load(diction)
# print(load(*diction[1]))

