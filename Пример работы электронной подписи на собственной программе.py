import hashlib


# Функция дешифрования
def decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isupper():
            c_index = ord(c) - ord('A')
            # sсдвинуть текущий символ влево на позицию клавиши, чтобы получить его исходное положение
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            # если это число, сдвиньте его фактическое значение
            c_og = (int(c) - key) % 10
            decrypted += str(c_og) 
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            decrypted += c
    return decrypted.lower()


def find_key(message,lang):
    key = []
    for i in range(1, 33):
        res = un_encryption(message, i, lang)
        if "ПРИВЕТ" in res or "HELLO" in res:
            key.append(i)

    return key


data = ''

with open("doc.txt", encoding='utf-8') as file:
    data = file.read()

hash_data = hashlib.md5(data.encode())
print(f"hash нашего файла: {hash_data.hexdigest()}")

with open("hash.txt", encoding='utf-8') as file:
    data_hash = file.read()

print(f"зашифрованный hash нашего файла: {data_hash}")

print(f"расшифрованный hash нашего файла: {decrypt(data_hash, 1)}")

if hash_data.hexdigest() == decrypt(data_hash, 1):
    print('Электронная подпись верна!')
else:
    print('Электронная подпись НЕ верна!')