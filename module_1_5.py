immutable_var = 6.9, 9, "шесть", [1, 2, 3]
print(immutable_var)
#immutable_var[0] = 76 - кортеж не поддерживает обращение по элементам
mutable_list = 6.9, 9, "шесть", [1, 2, 3,]
mutable_list[3][1] = 76
print(mutable_list)
