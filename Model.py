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
    for key1 in Items.keys():
        for key2 in Items[key1]:
            if Items[key1][key2].find(filter) >= 0:
                filter_items.update({key1 : Items[key1]})
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
   

ms = {
    1: {"Surname" : "Петров", "Name" : "Алексей", "MiddleName" : "Иванович", "BirthDay" : "", "EMail" : "petro@mail.ru", "Telephone" : "+79053284562", "Job" : "слесарь", "Note" : ""},
    2: {"Surname" : "Сидоров", "Name" : "Юрий", "MiddleName" : "Денисович", "BirthDay" : "06.08.1995", "EMail" : "sid123@list.ru", "Telephone" : "+79056837212", "Job" : "бухгалтер", "Note" : ""},     
      }
Init(ms)

# AddItem([10, "sdfdf", "123"])
print(DeleteItem(1))
print(GetItems(""))

# # st = "fdzxc"
# # print(st.find("zxc"))
