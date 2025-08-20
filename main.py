import random
import time

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += chars[random.randint(0, len(chars) - 1)]
    return password


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

print('Я создаю безопасные пароли и делаю это очень хорошо!')
time.sleep(1)

while True:
    try:
        q_pass = int(input('Сколько паролей вам нужно? '))
        break
    except ValueError:
        print('Пожалуйста, введите число!')

while True:
    if q_pass == 1:
        try:
            l_pass = int(input('Какой длины должен быть пароль? '))
            break
        except ValueError:
            print('Пожалуйста, введите число!')
    elif q_pass > 1:
        try:
            l_pass = int(input('Какой длины должны быть пароли? '))
            break
        except ValueError:
            print('Пожалуйста, введите число!')

add_digits = input('Включать ли цифры 0123456789? (y/n) ')
if add_digits == 'y':
    chars += digits
elif add_digits == 'n':
    print('Числа не добавлены')
    time.sleep(1)

add_up_alpha = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
if add_up_alpha == 'y':
    chars += uppercase_letters
elif add_up_alpha == 'n':
    print('Прописный буквы не добавлены')
    time.sleep(1)

add_lo_alpha = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
if add_lo_alpha == 'y':
    chars += lowercase_letters
elif add_lo_alpha == 'n':
    print('Строчные буквы не добавлены')
    time.sleep(1)

add_sym = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
if add_sym == 'y':
    chars += punctuation
elif add_sym == 'n':
    print('Специальные символы не добавлены')
    time.sleep(1)

del_sym = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')
if del_sym == 'y':
    for ch in 'il1Lo0O':
	    chars = chars.replace(ch, '')
elif del_sym == 'n':
    print('Неоднозначные символы не удалены')
    time.sleep(1)

if q_pass == 1:
    print('Ожидайте. Ваш пароль скоро будет готов...')
    time.sleep(1)
elif q_pass > 1:
    print('Ожидайте. Ваши пароли скоро будут готовы...')
    time.sleep(1)

for _ in range(q_pass):
    print(generate_password(l_pass, chars))