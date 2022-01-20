def personal_info(name, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')
personal_info(
    name = input('Имя: '),
    lastname = input('Фамилия: '),
    year_of_birth = input('Год Рождения: '),
    city = input('Город проживания: '),
    email = input('email: '),
    phone = input('phone: '))