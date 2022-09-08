# модуль интерфейса взаимодействия с пользователем


# Функция отрисовки меню 
# CommandList - список команд меню ["1 - Фильтр", "2 - Удалить", "3 - Добавить", "4 - Редактировать", ...]
def DrawMenu(CommandList : list):
    None

# Вывод строк данных (items) БД в виде таблицы
#-----------------------------------------------------------------------------------
#   ID : Surname | Name | MiddleName | BirthDay | EMail | Telephone | Job | Note| 
#   1    kjjkjk  | fhgf | iuhyiu     | yutuyt   
#   2    kjjkjk  | fhgf | iuhyiu     | yutuyt
#   3    kjjkjk  | fhgf | iuhyiu     | yutuyt
def DrawItems(items : dict):
    None

# Пользовательский ввод
# Возвращает строку текста, введенную пользователем
# prompt - строка текста, поясняющая ввод
def InputString(prompt : str):
    s : str = ""
    return s

# Функция очистки экрана
def ClearScreen():
    None
    
    
