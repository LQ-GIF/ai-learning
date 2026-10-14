from math import pi

# 计算圆的面积
def y_area(r):
    """计算圆的面积, r 是半径"""
    return round(pi * r ** 2, 2)

# 计算圆的周长
def y_perimeter(r):
    """计算圆的周长, r 是半径"""
    return round(2 * pi * r, 2)