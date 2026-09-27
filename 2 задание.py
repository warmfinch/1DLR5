
a, b, c = map(int, input("Введите три целых числа через пробел: ").split())

ab = a * b
bc = b * c
ca = c * a

a_pow = a ** 4      
b_mod = b % c       
c_div = c // a      

print(f"{a} * {b} = {ab}")
print(f"{b} * {c} = {bc}")
print(f"{c} * {a} = {ca}")
print(f"{a} ** 4 = {a_pow}")
print(f"{b} % {c} = {b_mod}")
print(f"{c} // {a} = {c_div}")
print(f"Сумма промежуточных переменных ({a_pow} + {b_mod} + {c_div}) = {a_pow + b_mod + c_div}")