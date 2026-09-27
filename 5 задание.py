import random
import string

def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string
message = input("Введите сообщение: ")
n = int(input("Введите количество подстановочных символов: "))
encoded_message = ''

for letter in message:
    encoded_message += letter + generate_random_string(n)
print("Кодированное послание:", encoded_message)
