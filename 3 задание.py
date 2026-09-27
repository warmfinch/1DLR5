full_name = input("Введите ФИО через пробел: ")

surname, name, patronymic = full_name.split()

print(surname.upper())
print(name.upper())
print(patronymic.upper())