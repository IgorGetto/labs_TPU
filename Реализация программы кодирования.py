
alfavit_EN =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' # длина 52
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' # длина 66

key = int(input('Шаг(ключ) шифровки: '))
message = input("Сообщение для шифровки: ").upper()
itog = ''
lang = input('Выберите язык RU/EN: ')   #Добавляем возможность выбора языка


def encryption(message, key, lang):
    itog = ''
    if lang == 'RU':
        for i in message:
            mesto = alfavit_RU.find(i)   # Алгоритм для шифрования сообщения на русском
            new_mesto = mesto + key
            if i in alfavit_RU:
                itog += alfavit_RU[new_mesto]
            else:
                itog += i
    else:
        for i in message:
            mesto = alfavit_EN.find(i)		# Алгоритм для шифрования сообщения на английском
            new_mesto = mesto + key
            if i in alfavit_EN:
                itog += alfavit_EN[new_mesto]
            else:
                itog += i
    return itog


def un_encryption(message,key,lang):
    itog = ''
    if lang == 'RU':
        for i in message:
            mesto = alfavit_RU.find(i)
            new_mesto = mesto - key  # Меняем знак + на знак -
            if i in alfavit_RU:
                itog += alfavit_RU[new_mesto]
            else:
                itog += i
    else:
        for i in message:
            mesto = alfavit_EN.find(i)  # Меняем знак + на знак -
            new_mesto = mesto - key
            if i in alfavit_EN:
                itog += alfavit_EN[new_mesto]
            else:
                itog += i
    return itog

# максимальный ключ - 32 (в русском алфавите)
def find_key(message,lang):
    key = []
    for i in range(1, 33):
        res = un_encryption(message, i, lang)
        if "ПРИВЕТ" in res or "HELLO" in res:
            key.append(i)

    return key


test = encryption(message, key, lang)
print(f"зашифрованая строка - {test}")

try:
    key = int(find_key(test,lang)[0])
    print(f"используемый ключ - {key}")
except IndexError:
    print(f"вот список ключей: {key}")


res_test = un_encryption(test, key, lang)
print(f"расшифрованая строка - {res_test}")


