import sqlite3

# A4
connect = sqlite3.connect('User.db')

# Рука с Ручкой
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
               ''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            subject VARCHAR (50) NOT NULL,
            grade INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
            ''')

connect.commit()

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

# add_user("Ardager", 23, "плавать")
# add_user("Altynai", 28, "рисовать")
# add_user("Begimay", 27, "читать")
# add_user("Umut", 21, "рисовать")
# add_user("Shirin", 14, "спорт")

def add_grade(user_id, subject, grade):
    cursor.execute('''
            INSERT INTO grades(user_id, subject, grade) VALUES (?,?,?)
                    ''',
                   (user_id, subject, grade))
    connect.commit()
    print(f'Оценка добавлена для пользователя с ID {user_id}')

# add_grade(1,'Алгебра', 3)
# add_grade(2,'Алгебра', 5)
# add_grade(3,'Алгебра', 4)
# add_grade(4,'Алгебра', 5)
# add_grade(5,'Алгебра', 4)
#
# add_grade(1,'Информатика', 5)
# add_grade(2,'Информатика', 4)
# add_grade(3,'Информатика', 5)
# add_grade(4,'Информатика', 5)


# JOIN

#users.age, users.hobby - можно добавить другие столбцы
def get_users_with_grades():
    cursor.execute('''
        SELECT users.name, grades.subject, grades.grade 
         FROM users
         LEFT JOIN grades ON users.user_id = grades.user_id ''')

    users = cursor.fetchall()
    for i in users:
        print(f'NAME: {i[0]}, SUBJECT: {i[1]}, GRADE: {i[2]}')

get_users_with_grades()

""" LESSON8 """
''' Агрегационные функции, Вложенные запросы, Views (представления)'''
#AVG () - среднее значение
#MAX () - максимально значение
#MIN () - минимальное значение
#COUNT () - количество
#SUM () - сумма


def get_average_grade():
    cursor.execute('SELECT AVG(grade) FROM grades')
    avg_grade = cursor.fetchone()

    print(f'Средний балл за ДЗ {avg_grade}')


#get_average_grade()

def get_count_users():
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()

    print(f'Количество пользователей {count}')
get_count_users()

def get_users_with_highest_grade():
    cursor.execute('''
        SELECT name, subject, grade
        FROM users
        JOIN grades ON users.user_id = grades.user_id 
        WHERE grade = (SELECT MAX(grade) FROM grades)''')

    users = cursor.fetchall()

    for i in users:
        print(f'NAME: {i[0]}, SUBJECT: {i[1]}, GRADE: {i[2]}')

get_users_with_highest_grade()

# Views (Представления)

def create_young_users_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS young_users AS
        SELECT name, age, hobby FROM users
        WHERE age <25
                    ''')

    connect.commit()
    print(f'Представление создано!')

create_young_users_view()


def get_young_users():
    cursor.execute('SELECT * FROM young_users')
    users = cursor.fetchall()

    print(f'Молодые пользователи до 25 лет!')
    for i in users:
        print(f'NAME: {i[0]}, AGE: {i[1]}, HBY: {i[2]}')
get_young_users()



