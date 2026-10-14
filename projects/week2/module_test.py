# module_test.py - 模块导入练习
# 练习：import math、from...import、导入自己写的模块、__name__判断

# ========== 练习1：import math（整个模块导入）==========
print("【练习1】import math - 整个模块导入")
import math

# 使用时必须加 math. 前缀
print(f"16的平方根: {math.sqrt(16)}")
print(f"圆周率π: {math.pi}")
print(f"π/2的正弦值: {math.sin(math.pi / 2)}")
print(f"e 的自然常数: {math.e}")
print(f"9的平方根: {math.sqrt(9)}")

# ========== 练习2：from math import ...（只导入需要的）==========
print("\n【练习2】from math import - 只导入需要的函数")
from math import sqrt, pi, sin, cos

# 使用时直接写函数名，不需要 math. 前缀
print(f"25的平方根: {sqrt(25)}")
print(f"圆周率π: {pi}")
print(f"π的正弦值: {sin(pi)}")
print(f"0的余弦值: {cos(0)}")

# ========== 练习3：导入自己写的模块 geometry ==========
print("\n【练习3】导入自己写的模块 geometry")
import geometry

# 使用 geometry 模块里的函数
print(f"半径为10的圆面积: {geometry.circle_area(10)}")
print(f"半径为8的圆周长: {geometry.circle_perimeter(8)}")
print(f"宽5高8的矩形面积: {geometry.rectangle_area(5, 8)}, 周长: {geometry.rectangle_perimeter(5, 8)}")
print(f"底4高9的三角形面积: {geometry.triangle_area(4, 9)}")
print(f"三边3、4、5的三角形面积 (海伦公式): {geometry.triangle_area_heron(3, 4, 5)}")

# ========== 练习4：from geometry import ...（从自己的模块只导入需要的）==========
print("\n【练习4】from geometry import - 从自己的模块只导入需要的函数")
from geometry import circle_area, triangle_area

# 直接使用，不需要 geometry. 前缀
print(f"半径为7的圆面积: {circle_area(7)}")
print(f"  底6高9的三角形面积: {triangle_area(6, 9)}")

# ========== 练习5：验证 __name__ 的值 ==========
print("\n【练习5】验证 __name__ 的值")
print(f"module_test 的 __name__ 是: {__name__}")
print(f"geometry 的 __name__ 是: {geometry.__name__}")
print(f"   (因为 module_test 是直接运行的，所以 __name__ = '__main__') ")
print(f"   (geometry 是被导入的，所以 __name__ = 'geometry') ")

# ========== 练习6：pip 安装的第三方库 requests ==========
print("\n【练习6】第三方库 requests (需要先 pip install requests) ")
try:
    import requests
    print(f"  requests 库导入成功！版本：{requests.__version__}")
    print(f"  requests 库的位置：{requests.__file__}")
except ImportError:
    print("  requests 库未安装, 请先运行: pip install requests")

# ========== 练习7：导入自己写的包，从包中调用模块 geometry ==========
print("\n【练习7】导入自己写的包 Geometric functions, 从包中调用模块 ")

# ========== 计算圆的面积周长 ==========
import Geometric_functions.circle
print(f"半径为12的圆的面积为: {Geometric_functions.circle.y_area(12)}, 周长为: {Geometric_functions.circle.y_perimeter(12)}")

# ========== 计算矩形的面积周长 ==========
from Geometric_functions import rectangle
print(f"宽6高9的矩形的面积为: {rectangle.jx_area(6, 9)}, 周长为: {rectangle.jx_perimeter(6, 9)}")

# ========== 计算三角形的面积周 ==========
from Geometric_functions.triangle import sjx_area
print(f"底6高10的三角形的面积为: {sjx_area(6, 10)}")

from Geometric_functions.triangle import sjx_area_heron
print(f"三边分别为4, 9, 11的三角形的面积为: {sjx_area_heron(4, 9, 11)}")



# ========== 主程序入口 ==========
if __name__ == "__main__":
    print("\n" + "=" * 40)
    print("  所有模块导入练习完成！")
    print("=" * 40)