from math import sqrt

# 计算三角形的面积（底乘高除以2）
def sjx_area(b, h):
    """计算三角形面积, b 是底, h 是高"""
    return b * h / 2

# 已知三角形三边，用海伦公式计算面积
def sjx_area_heron(a, b, c):
    """
    用海伦公式计算三角形面积
    a, b, c 是三角形的三条边
    """
    s = (a + b + c) / 2   # 半周长
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area