import sqlite3

# A4
connect = sqlite3.connect('User.db')

# Рука с Ручкой
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
               ''')

# Сохранение изменений
connect.commit()


# CRUD - Create - Read - Update - Delete


# Create
def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")


# name = input("Введите имя")
# age = input("Введите возраст")
# hobby = input("Введите Хоби")

# add_user("ardager", 23, "плавать")
# add_user("altynai", 28, "рисовать")
# add_user("begimay", 27, "читать")
# add_user("umut", 21, "рисовать")
# add_user("shirin", 14, "спорт")


def get_all_users():
    cursor.execute('SELECT name, age, hobby FROM users')
    users = cursor.fetchall()
    print(users)
    print('Список всех пользователей')

    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")


# get_all_users()


# Функция для поиска пользователя по имени
def get_user_by_name(name):
    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
    user = cursor.fetchall()
    if user:
        return f"NAME: {user[0][0]}, AGE: {user[0][1]}, HOBBY: {user[0][2]}"
    else:
        return "Пользователь не найден"


# Тест функции
# print(get_user_by_name('ardager'))


#Update

# def update_user(new_name, row_id):
#
#     cursor.execute (
#         'UPDATE users SET name = ?, WHERE rowid = ?', (new_name, row_id)
#     )
#     connect.commit()
#     print('User_Updated!')
#
# update_user(row_id=1, new_name = 'TEST')
#
# #Delete
# def delete_user(row_id):
#     cursor.execute (
#         'DELETE from users WHERE rowid = ?', (row_id)
#     )
#     connect.commit()
#     print('User_Deleted')



def update_user(new_name, id):

    cursor.execute (
        'UPDATE users SET name = ?, WHERE id = ?', (new_name, id)
    )
    connect.commit()
    print('User_Updated!')

update_user(id=1, new_name = 'TEST')

#Delete
def delete_user(id):
    cursor.execute (
        'DELETE from users WHERE rowid = ?', (id)
    )
    connect.commit()
    print('User_Deleted')