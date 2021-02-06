#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Известна стоимость монитора, системного блока, клавиатуры и мыши.
# Сколько будут стоить 3 компьютера из этих элементов? N компьютеров?

if __name__ == '__main__':
    Monitor = float(input("Введите стоимость монитора"))
    SistemBlok = float(input("Введите стоимость системного блока"))
    Klava = float(input("Введите стоимость клавиатуры"))
    Mouse = float(input("Введите стоимость мышки"))
    # Cтоимость одного компа
    Sum = Monitor + SistemBlok + Klava + Mouse
    # Cтоимость трёх компьютеров
    TriCompa = Sum*3
    N = float(input("Введите кол-во компьютеров"))
    NComp = Sum*N
    print("Cтоимость одного компьютера", Sum)
    print("Cтоимость трёх компьютеров", TriComp)
    print("Cтоимость N кол-ва компьютеров", NComp)
