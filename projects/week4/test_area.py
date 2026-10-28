"""
test_area.py - area.py 的测试考卷
pytest 规则：文件名 test_ 开头，测试函数 test_ 开头
"""
import math
import area
import pytest

def test_rectangle_normal():
    """正常输入: 3x4 的矩形，面积应该是 12"""
    assert area.calculate_rectangle_area(3, 4) == 12

def test_rectangle_boundary():
    """边界值: 一边为 0, 面积应该是 0"""
    assert area.calculate_rectangle_area(0, 5) == 0
    assert area.calculate_rectangle_area(3, 0) == 0
    assert area.calculate_rectangle_area(0, 0) == 0

def test_circle_radius_one():
    """正常输入: 半径为 1 的圆, 面积应该约等于 π"""
    result = area.calculate_circle_area(1)
    assert abs(result - math.pi) < 0.0001

def test_rectangle_negative_raises():
    """异常测试：矩形传负数，必须抛出 ValueError"""
    with pytest.raises(ValueError):
        area.calculate_rectangle_area(-3, 4)

def test_circle_negative_raises():
    """异常测试：圆半径为负数，必须抛出 ValueError"""
    with pytest.raises(ValueError):
        area.calculate_circle_area(-1)

def test_circle_none_raises():
    """异常测试：圆半径为空值，必须抛出 TypeError"""
    with pytest.raises(TypeError):
        area.calculate_circle_area()

