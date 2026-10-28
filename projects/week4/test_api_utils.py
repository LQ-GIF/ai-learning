"""
test_api_utils.py - api_utils.py 的参数校验测试
注意: api_utils.py 在 projects/week3/ 目录，需要先告诉 Python 去哪里找
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "week3"))
from api_utils import api_call

def test_method_delete_raises():
    """非法 method: DELETE 不在 GET/POST 之列，必须 raise ValueError"""
    with pytest.raises(ValueError):
        api_call(method="DELETE", url="https://example.com")

def test_method_put_raises():
    """非法 method: PUT 同样不支持"""
    with pytest.raises(ValueError):
        api_call(method="PUT", url="https://example.com")

def test_method_weird_raises():
    """非法 method: 随便传个乱码字符串"""
    with pytest.raises(ValueError):
        api_call(method="ADD", url="https://example.com")