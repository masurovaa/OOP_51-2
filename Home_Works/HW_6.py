import sqlite3

# А4
connect = sqlite3.connect('User.db')

#Рука с ручкой
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR(40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')

#Сохранение изменений
connect.commit()

# CRUD - Create - Reate - Update - Delete

# Create -Функция для добавления пользователя
def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")


#
# add_user("Ардагер", 23, "плавать")
# add_user("Алтынай", 28, "рисовать")


# Функция для получения всех пользователей
def get_all_users():
    cursor.execute('SELECT name, age, hobby FROM users')
    users = cursor.fetchall()
    print(users)
    print('Список всех пользователей')

    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")


#get_all_users()

# Функция для поиска пользователя по имени
def get_user_by_name(name):
    cursor.execute('SELECT name, age, hobby FROM users WHERE name = ?', (name,))
    user = cursor.fetchall()
    if user:
        return f"NAME: {user[0][0]}, AGE: {user[0][1]}, HOBBY: {user[0][2]}"
    else:
        return "Пользователь не найден"


# Тест функции
print(get_user_by_name('Алтынай'))
