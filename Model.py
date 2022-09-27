# Функционал модели информационной системы

Items = {}  # глобальный словарь БД
global Filter
Filter = ""


#
def Init(items: dict):
    """ инициализация БД (словаря) """
    global Items
    Items = items.copy()


#
def GetItems(filter: str):
    """ Возврат списка записей (словарь) удовлетворяющих фильтру. """
    filter_items = {}
    if filter == "":
        return Items
    for key1 in Items.keys():
        for key2 in Items[key1]:
            if Items[key1][key2].find(filter) >= 0:
                filter_items.update({key1: Items[key1]})
                break
    return filter_items


def AddItem(dic: dict):
    """ Добавление записи в словарь (если ID == 0) иначе изменение существующей """
    new_id = list(dic.keys())[0]
    data = dic[new_id]
    if new_id == 0:
        new_id = 1
        while True:
            if new_id not in Items.keys():
                break
            new_id += 1
    Items.update({new_id: data})


#
def DeleteItem(id: int):
    """Удаление записи по ID"""
    return Items.pop(id, None) != None


#
def GetEmptyItem() -> dict:
    """Возвращает пустую запись БД."""
    return {0: {"Surname": "Фамилия", "Name": "Имя", "MiddleName": "Отчество",
                "BirthDay": "День рождения", "EMail": "Email",
                "Telephone": "Телефон", "Job": "Профессия", "Note": "Заметки"}}



def CheckID(id: int) -> bool:
    """ Проверка на существование записи с указанным ID."""
    return id in Items.keys()
