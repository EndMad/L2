a1 = int(input("Введите число единиц "))
a2 = int(input("Введите число десяток "))
b = int(input("Введите однозначное число "))

cu1 = (a1 + b) % 10
cu2 = (a2 + (a1 + b)) // 10

print("Цифры полученного числа {0}{1}".format(cu2, cu1))
