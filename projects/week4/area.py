"""
area.py - 面积计算 v2 (main 分支修改)
"""
import math
def calculate_rectangle_area(length: float, width: float) -> float:
    """计算矩形面积：长 x 宽。

    参数:
        length: 长度
        width: 宽度
    返回:
        面积
    """
    if length < 0 or width < 0:
        raise ValueError("长和宽不能为负数")
    return length * width

def calculate_circle_area(radius: float) -> float:
    """计算圆形面积：π x 半径²。"""
    if radius < 0:
        raise ValueError("圆的半径不能为负数")
    return math.pi * radius ** 2

if __name__ == "__main__":
    print(f"矩形 3x4 面积: {calculate_rectangle_area(3, 4)}")
    print(f"圆形 r=1 面积: {calculate_circle_area(1)}")