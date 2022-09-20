# Функционал модели информационной системы

Items = {}  # глобальный словарь БД
global Filter
Filter = ""


# инициализация БД (словаря)
def Init(items: dict):
    global Items
    Items = items.copy()


# возврат списка записей (словарь) удовлетворяющих фильтру
def GetItems(filter: str):
    filter_items = {}
    if filter == "":
        return Items
    for key1 in Items.keys():
        for key2 in Items[key1]:
            if Items[key1][key2].find(filter) >= 0:
                filter_items.update({key1: Items[key1]})
                break
    return filter_items


# Добавление записи в словарь (если ID == 0) иначе изменение существующей
def AddItem(dic: dict):
    NewID = list(dic.keys())[0]
    data = dic[NewID]
    if NewID == 0:
        NewID = 1
        while True:
            if NewID not in Items.keys():
                break
            NewID += 1
    Items.update({NewID: data})


# Удаление записи по ID
def DeleteItem(id: int):
    return Items.pop(id, None) != None


# Возвращает пустую запись БД
def GetEmptyItem() -> dict:
    return {0: {"Surname": "Фамилия", "Name": "Имя", "MiddleName": "Отчество", "BirthDay": "День рождения", "EMail": "Email", "Telephone": "Телефон", "Job": "Профессия", "Note": "Заметки"}}


# проверка на существование записи с указанным ID
def CheckID(id: int):
    return id in Items.keys()
