def get_num():
    id = ''
    while type(id) != int:
        try:
            id = int(input('input ID: '))
        except:
            print('Введите целое число')

    return id


def create_user():
    columns = ['id', 'surname', 'name', 'middlename', 'birthday', 'email', 'telephone', 'job', 'note']
    user_data = {}
    for column in range(len(columns)):
        if column == 0:
            id = get_num()
            user_data[columns[0]] = id
        else:
            cell = input(f'input {columns[column]}: ')
            user_data[columns[column]] = cell
    return str(user_data)


if __name__ == "__main__":

    with open('base', 'a', encoding='utf-8') as f:
        f.write(f'{create_user()}\n')
