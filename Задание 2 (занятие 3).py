# ---- Мое решение ----

def my_input ():
    name = input('введите имя: ')
    surname = input('введите фамилию: ')
    year = input('введите год рождения: ')
    city = input('введите город проживания: ')
    email = input('введите email: ')
    tel = input('введите номер телефона: ')
    return name, surname, year, city, email, tel

def my_print (name = '', surname = '', year = '', city = '', email = '', tel = ''):
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город проживания: {city}, email: {email}, Телефон: {tel}')

def main():
    a, b, c, d, e, f = my_input()
    my_print(name = a, surname = b, year = c, city = d, email = e, tel = f)

main()
# ---- Конец моего решения ----


'''
# ---- Решение Евгения ---
def person_inf(name, surname, birthday, city, email, phone):
    return f'Name - {name}; Surname - {surname}; Birthday - {birthday}; City - {city};'\
           f'Email - {email}; Phone - {phone}'

def personal_inf(**kwargs):
    return ' '.join(kwargs.values())

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birthday = input('Введите год рождения: ')
city = input('Введите место жительства: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')

print(personal_inf(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))

# ---- Конец решения Евгения ---
'''