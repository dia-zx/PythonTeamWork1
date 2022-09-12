# Функционал модели информационной системы

Items = {} # глобальный словарь БД

# инициализация БД (словаря)
def Init(items : dict):
    global Items
    Items = items.copy()
    

# возврат списка записей (словарь) удовлетворяющих фильтру
def GetItems(filter : str):
    filter_items = {}
    if filter == "":
        return Items
    for key in Items.keys():
        for item in Items[key]:
            if item.find(filter) >= 0:
                filter_items.update({key : Items[key]})
                break
    return filter_items


# Добавление записи в словарь (если ID == 0) иначе изменение существующей
def AddItem(ls : list):
    NewID = ls[0]
    if ls[0] == 0:
        NewID = 0
        while True:
            if NewID not in Items.keys():
                break
            NewID += 1
    Items.update({NewID : ls[1:]})
            
    

#Удаление записи по ID
def DeleteItem(id : int):
    return Items.pop(id, None) != None
   

# ms = {1: ["Иванов", "Сергеевич", "+7899"]}
# ms.update({2: ["Петров", "Иванович", "+7890"]})
# Init(ms)

# AddItem([10, "sdfdf", "123"])
# #print(DeleteItem(1))
# print(GetItems(""))

# # st = "fdzxc"
# # print(st.find("zxc"))
