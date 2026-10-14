import math

# 计算圆的面积
def circle_area(radius):
    """计算圆的面积, radius 是半径"""
    return round(math.pi * radius ** 2, 2)

# 计算圆的周长
def circle_perimeter(radius):
    """计算圆的周长, radius 是半径"""
    return round(2 * math.pi * radius, 2)

# 计算矩形的面积
def rectangle_area(width, height):
    """计算矩形的面积, width 是宽, height 是高"""
    return width * height

# 计算矩形的周长
def rectangle_perimeter(width, height):
    """计算矩形的周长, width 是宽, height 是高"""
    return (width + height) * 2

# 计算三角形的面积（底乘高除以2）
def triangle_area(base, height):
    """计算三角形面积, base 是底, height 是高"""
    return base * height / 2

# 已知三角形三边，用海伦公式计算面积
def triangle_area_heron(a, b, c):
    """
    用海伦公式计算三角形面积
    a, b, c 是三角形的三条边
    """
    s = (a + b + c) / 2   # 半周长
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# 测试代码：只有直接运行这个文件时才执行

if __name__ == "__main__":
    print("=" * 40)
    print("  geometry 模块自测")
    print("=" * 40)

    print(f"\n半径为5的圆: ")
    print(f"面积为: {circle_area(5)}")
    print(f"周长为: {circle_perimeter(5)}")

    print(f"\n宽为4、高为6的矩形: ")
    print(f"面积为: {rectangle_area(4, 6)}")
    print(f"周长为: {rectangle_perimeter(4, 6)}")

    print(f"\n底为3、高为4的三角形: ")
    print(f"面积为: {triangle_area(3, 4)}")

    print(f"\n三边为3、4、5的三角形 (海伦公式): ")
    print(f"面积为: {triangle_area_heron(3, 4, 5)}")

    print("\n自测完成!")