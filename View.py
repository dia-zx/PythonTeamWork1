# модуль интерфейса взаимодействия с пользователем
from os import system

# Функция отрисовки меню 
# CommandList - список команд меню ["1 - Фильтр", "2 - Удалить", "3 - Добавить", "4 - Редактировать", ...]
def DrawMenu(CommandList : list):
    print(CommandList)

# Вывод строк данных (items) БД в виде таблицы
#-----------------------------------------------------------------------------------
#   ID : Surname | Name | MiddleName | BirthDay    | EMail      | Telephone | Job           | Note      | 
#   1    Иванов  | Иван | Петрович   | 10.10.2010  |апа@fgd.net |+7908885751|программист    | холостой) |
#   1    Петров  | Иван | Петрович   | 10.10.2010  |апа@fgd.net |+7908885751|программист    | с юмором  |
#   1    Сидоров | Иван | Петрович   | 10.10.2010  |апа@fgd.net |+7908885751|программист    | женат     |
def DrawItems(items : dict):
    ColumnWidth = [4, 20, 15, 20, 12, 15, 14, 15, 25]
    ColumnsTitle = ["ID", "Фамилия", "Имя", "Отчество", "д. рожд.", "Email", "Телефон", "Профессия", "Заметки"]
    # ****************** Заголовок таблицы **********************
    st = ""
    for it in ColumnWidth:
        st += "╦" + "═"*it
    st = "╔" + st[1:]
    st += "╗"
    print(st)
    
    st = ""
    for i in range(len(ColumnsTitle)):
        st += "║" + ColumnsTitle[i].center(ColumnWidth[i], " ")
    st += "║"
    print(st)
    
    st = ""
    for it in ColumnWidth:
        st += "╬" + "═"*it
    st = "╠" + st[1:]
    st += "╣"
    print(st)
      
    # ***************** Записи БД *****************************
    for key in items.keys():
        st = "║" + str(key).center(ColumnWidth[0])
        i = 1
        for key2 in items[key].keys():
            st += "║" + items[key][key2].center(ColumnWidth[i], " ")
            i += 1
        st += "║"
        print(st)
            
    # ***************** Нижняя строка таблицы   *****************
    st = ""
    for it in ColumnWidth:
        st += "╩" + "═"*it
    st = "╚" + st[1:]
    st += "╝"
    print(st)


# Пользовательский ввод
# Возвращает строку текста, введенную пользователем
# prompt - строка текста, поясняющая ввод
def InputString(prompt : str):
    return input(prompt)

# Функция очистки экрана
def ClearScreen():
    system('cls||clear')
    
    
    
# ms = {
#     1: {"Surname" : "Петров", "Name" : "Алексей", "MiddleName" : "Иванович", "BirthDay" : "", "EMail" : "petro@mail.ru", "Telephone" : "+79053284562", "Job" : "слесарь", "Note" : ""},
#     2: {"Surname" : "Сидоров", "Name" : "Юрий", "MiddleName" : "Денисович", "BirthDay" : "06.08.1995", "EMail" : "sid123@list.ru", "Telephone" : "+79056837212", "Job" : "бухгалтер", "Note" : ""},     
#       }    
# ClearScreen()    
# DrawItems(ms)