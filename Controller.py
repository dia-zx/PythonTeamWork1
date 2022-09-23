# Основная логика поведения

import FileIO
import Model
import View


# основной циклический метод
def Start():
   # Model.Init(FileIO.Load())
    ms = {
        1: {"Surname": "Петров", "Name": "Алексей", "MiddleName": "Иванович", "BirthDay": "", "EMail": "petro@mail.ru", "Telephone": "+79053284562", "Job": "слесарь", "Note": ""},
        2: {"Surname": "Сидоров", "Name": "Юрий", "MiddleName": "Денисович", "BirthDay": "06.08.1995", "EMail": "sid123@list.ru", "Telephone": "+79056837212", "Job": "бухгалтер", "Note": ""},
    }
    Model.Init(ms)
    while (True):
        View.ClearScreen()
        View.DrawItems(Model.GetItems(Model.Filter), Model.Filter)
        View.DrawMenu(["1 Добавить", "2 Редактировать", "3 Удалить",
                      "4 Фильтр", "5 Сохранить", "6 Загрузить", "0 Выход"])
        input = View.InputString("Введите действие: ")

        # ******* Выход **************
        if input == "0":
            print("Работа с БД завершена!")
            break

        # ********* Удаление ***********
        if input == "3":
            input = View.InputString("Введите ID: ")
            res = Model.DeleteItem(int(input))
            if not res:
                View.InputString(
                    "Ошибка. Введен неверный ID! Нажмите <Enter>:")
            continue

        # **************** Фильтр ****************
        if input == "4":
            input = View.InputString("Введите значение фильтра: ")
            Model.Filter = input
            continue

        # **************** Добавить ****************
        if input == "1":
            newrecord = Model.GetEmptyItem()
            for key in newrecord[0].keys():
                newrecord[0][key] = View.InputString(newrecord[0][key] + ": ")
            Model.AddItem(newrecord)
            continue

        # **************** Редактировать ****************
        if input == "2":
            id = int(View.InputString("Введите ID записи для редактирования: "))
            if Model.CheckID(id) == False:
                View.InputString(
                    "Ошибка. Введен неверный ID! Нажмите <Enter>:")
                continue
            newrecord = Model.GetEmptyItem()
            for key in newrecord[0].keys():
                newrecord[0][key] = View.InputString(newrecord[0][key] + ": ")
            Model.AddItem({id: newrecord[0]})
            continue

        # **************** Сохранить ****************
        if input == "5":
            FileIO.save(Model.GetItems(""))
            continue

        # **************** Загрузить ****************
        if input == "6":
            Model.Init(FileIO.load())
            continue
