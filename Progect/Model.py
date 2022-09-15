# Функционал модели информационной системы

Items = {}  # глобальный словарь БД

# инициализация БД (словаря)
def Init(items : dict):
    global Items
    Items = items.copy()
    

# возврат списка записей (словарь) удовлетворяющих фильтру
def GetItems(filter : str):
    filter_items = {}
    None
    return filter_items


def AddItem(ls : list):
    None


def DeleteItem(id):
    None
    return True