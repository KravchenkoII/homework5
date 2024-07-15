immutable_var = ("сматрфон","computer",12,48, True)
print(immutable_var)

# immutable_var[0]="планшет"
# Данные в переменной immutable_var относятся к не изменяемому типу - кортеж. Выполенние этой команды приведет
# к ошибке и остановке программы

mutable_list = [543, 8354, "notebook", "машина", False]
print(mutable_list)
mutable_list[0] = "корова"
mutable_list[2] = False
mutable_list[3] = 10101010
mutable_list[4] = "notebook"
print(mutable_list)