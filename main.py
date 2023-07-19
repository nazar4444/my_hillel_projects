import random

DIGITS = "1234567890"
SMALL_LETTERS = "abcdefghijklmnopqrstuvwxyz"
BIG_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
EXTRA_CHARS = "+-/*!№;%:?*()="

ALL_CHARS = DIGITS + SMALL_LETTERS + BIG_LETTERS + EXTRA_CHARS


def check_password(user_password):
    has_digit = False
    has_small_letter = False
    has_big_letters = False
    has_extra_chars = False

    if len(user_password) < 8:
        return "Длинна пароля должна быть не меньше"

    for symbol in user_password:
        if symbol not in ALL_CHARS:
            return "Пароль не соответствует требованиям"

        if symbol in DIGITS:
            has_digit = True

        elif symbol in SMALL_LETTERS:
            has_small_letter = True

        elif symbol in BIG_LETTERS:
            has_big_letters = True

        else:
            has_extra_chars = True

    errors = []
    if has_digit == False:
        errors.append("Добавь в свой пароль цифры")

    if has_big_letters == False:
        errors.append("Добавь в свой пароль большие буквы")

    if has_small_letter == False:
        errors.append("Добавь в свой пароль маленькие буквы")

    if has_extra_chars == False:
        errors.append("Добавь в свой пароль специальные символы")

    if len(errors) > 0:
        return errors
    else:
        return "Пароль идеален"


password = input("Введите пароль: ")
reason = check_password(password)
print(reason)


def random_numbers() -> int:
    return random.randint(0, 1000)

