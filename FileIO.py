# Модуль взаимодействия с файловой системой

# функция записи базы данных в файл
# dic - словарь записей баз данных 
# dic ~ 
# {
    # ID : 
    # {
        # "Surname" : "",
        # "Name" : "" ,
        # "MiddleName : "",
        # "BirthDay : "",
        # "EMail : "",
        # "Telephone : "",
        # "Job : "",
        # "Note : ""
    # }
    # ...
# }


def save(dic: dict):
    """ Сохранение информации в файл base. """
    with open('base', 'w', encoding='utf-8') as f:
        f.write(str(len(dic)) + '\n')
        for key_id in dic:
            f.write(str(key_id) + '\n')
            f.write(str(len(dic[key_id])) + '\n')
            for key2_id in dic[key_id]:               # подсловарь
                f.write(str(key2_id) + '\n')
                f.write(dic[key_id][key2_id] + '\n')


def load() -> dict:
    """ Функция распаковки базы данных из файла.
        Возвращает dict """
    dic = {}
    with open('base', 'r', encoding='utf-8') as f:
        id_count = f.readline()
        id_count = int(id_count)
        for it in range(id_count):
            key_id = int(f.readline())
            id_count2 = f.readline()   # подсловарь
            id_count2 = int(id_count2)
            dic2 = {}                       # подсловарь
            for it2 in range(id_count2):    # подсловарь
                key_id2 = str.replace(f.readline(), '\n', '')
                value = str.replace(f.readline(), '\n', '')
                dic2[key_id2] = value
            dic[key_id] = dic2
    return dic


# ms = {
#         1: {"Surname": "Петров", "Name": "Алексей", "MiddleName": "Иванович", "BirthDay": "", "EMail": "petro@mail.ru", "Telephone": "+79053284562", "Job": "слесарь", "Note": ""},
#         2: {"Surname": "Сидоров", "Name": "Юрий", "MiddleName": "Денисович", "BirthDay": "06.08.1995", "EMail": "sid123@list.ru", "Telephone": "+79056837212", "Job": "бухгалтер", "Note": ""},
#     }
# save(ms)
# print(load())
