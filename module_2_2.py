first = int(input('первое число: '))
second = int(input('второе число: '))
third = int(input('третье число: '))

print('количество равных чисел')

if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)