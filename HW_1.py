import re

def register_user():
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$'

    while True:
        email = input("Введите вашу почту: ")
        if re.match(email_pattern, email):
            break
        else:
            print("Неправильный формат почты. Попробуйте еще раз.")

    while True:
        password = input("Введите пароль (минимум 8 символов, должен содержать хотя бы одну заглавную букву, одну строчную букву и одну цифру): ")
        if re.match(password_pattern, password):
            break
        else:
            print("Неправильный формат пароля. Попробуйте еще раз.")

    print("Регистрация успешна!")
    print("Почта:", email)
    print("Пароль:", password)

register_user()
input("press any key to close window")
