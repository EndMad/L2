#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Известна стоимость монитора, системного блока, клавиатуры и мыши.
# Сколько будут стоить 3 компьютера из этих элементов? N компьютеров?

if __name__ == '__main__':
    monitor = float(input("Введите стоимость монитора"))
    sistem_blok = float(input("Введите стоимость системного блока"))
    klava = float(input("Введите стоимость клавиатуры"))
    mouse = float(input("Введите стоимость мышки"))
    # Cтоимость одного компа
    sum_comp = monitor + sistem_blok + klava + mouse
    # Cтоимость трёх компьютеров
    tri_compa = sum_comp*3
    n = float(input("Введите кол-во компьютеров"))
    n_comp = sum_comp*n
    print("Cтоимость одного компьютера", sum_comp)
    print("Cтоимость трёх компьютеров",  tri_compa)
    print("Cтоимость N кол-ва компьютеров", n_comp)
