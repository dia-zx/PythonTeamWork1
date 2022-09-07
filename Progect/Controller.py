# Основная логика поведения

import FileIO
import Model
import View


Filter = ""

# основной циклический метод
def Start():
    Model.Init(FileIO.Load())
    while(True):
        View.ClearScreen()
        View.DrawItems(Filter)
        View.DrawMenu(["1 Добавить", "2 Удалить", "3 Фильтр", "4 Сохранить", "5 Загрузить", "0 Выход"])
        input = View.InputString("Введите действие:")
        None
        
    None
    