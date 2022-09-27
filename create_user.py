""" Функция получения возрастающего на 1 числа из файла"""


def num_from_id():
    with open('id', 'r', encoding='utf-8') as f:
        num_id = f.read()
        num_id = int(num_id) + 1
        num_id = str(num_id)
    with open('id', 'w', encoding='utf-8') as f:
        f.write(num_id)
    return int(num_id)


def create_user():
    columns = ['id', 'surname', 'name', 'middlename', 'birthday', 'email', 'telephone', 'job', 'note']
    user_data = {}
    for column in range(len(columns)):
        if column == 0:
            id = num_from_id()
            user_data[columns[0]] = id
        else:
            cell = input(f'input {columns[column]}: ')
            user_data[columns[column]] = cell
    return str(user_data)


if __name__ == "__main__":

    with open('base', 'a', encoding='utf-8') as f:
        f.write(f'{create_user()}\n')
