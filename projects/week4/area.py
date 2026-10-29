"""
area.py - 面积工具集 (含矩形/圆形/三角形)
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

def calculate_triangle_area(base: float, height: float) -> float:
    """计算三角形面积: 底 x 高 / 2"""
    if base < 0 or height < 0:
        raise ValueError("底和高不能为负数")
    return base * height / 2

if __name__ == "__main__":
    print(f"矩形 3x4 面积: {calculate_rectangle_area(3, 4)}")
    print(f"圆形 r=1 面积: {calculate_circle_area(1)}")
    print(f"三角形 3x4/2 面积: {calculate_triangle_area(3, 4)}")