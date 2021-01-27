#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Известна стоимость монитора, системного блока, клавиатуры и мыши.
# Сколько будут стоить 3 компьютера из этих элементов? N компьютеров?


Monitor = float(input("Введите стоимость монитора"))
S_blok = float(input("Введите стоимость системного блока"))
Klava = float(input("Введите стоимость клавиатуры"))
Mouse = float(input("Введите стоимость мышки"))

Sum = Monitor + S_blok + Klava + Mouse

Tri_comp = Sum * 3

N = float(input("Введите кол-во компьютеров"))
N_comp = Sum * N


print("Cтоимость одного компьютера", Sum)
print("Cтоимость трёх компьютеров", Tri_comp)
print("Cтоимость N кол-ва компьютеров", N_comp)

