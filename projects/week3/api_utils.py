"""
api_utils.py - 通用 API 调用工具模块

封装了状态码判断, 自动重试(指数退避), 统一异常处理
其他脚本通过 from api_utils import api_call 复用
"""

import time
import requests
from typing import Any, Dict, Optional

def api_call(
    method: str,
    url: str,
    params: Optional[Dict] = None,
    json: Optional[Dict] = None,
    headers: Optional[Dict] = None,
    timeout: int = 10,
    max_retries: int = 3
) -> Any:
    """
    发送 HTTP 请求的通用函数 (支持 GET/POST, 自动重试, 统一异常处理)

    参数:
        method: 请求方法, 'GET' 或 'POST' (不区分大小写)
        url: 请求地址
        params: URL 查询参数字典 (GET 请求使用), 可选
        json: 请求体数据字典(POST 请求使用, 自动转 JSON), 可选
        headers: 请求头字典, 可选
        timout: 超时秒数, 默认 10 秒
        max_retries: 最大重试次数, 默认 3 次
    
    返回:
        成功时返回解析后的响应 JSON (字典或列表)
        失败时返回 None (调用者需判断 None 再使用结果)

    异常处理策略:
        - Timeout 超时、ConnectionError 连接失败, 自动重试
        - 5xx 服务器错误: 自动重试, 重试间隔指数退避 (1s -> 2s -> 4s)
        - 4xx 客户端错误 (400/401/403/404等): 不重试, 直接返回 None
    """

    # 统一转大写，避免调用者写成 "get" / "post" 小写导致判断失败
    method = method.upper()

    # 校验请求方法是否支持
    if method not in ("GET", "POST"):
        raise ValueError(f"不支持请求方法: {method}, 仅支持 GET/POST")

    # 记录最后一次错误信息，重试耗尽后打印给用户看
    last_error = None

    # ===== 重试循环 =====
    for retry in range(1, max_retries + 1):
        try:
            if method == "GET":
                response = requests.get(
                    url,
                    params=params,
                    headers=headers,
                    timeout=timeout
                )
            else:
                response = requests.post(
                    url,
                    json=json,
                    headers=headers,
                    timeout=timeout
                )

            # ===== 4xx 客户端错误：重试没有意义，直接返回 None =====
            if 400 <= response.status_code <500:
                print(f"❌ 请求被拒绝 (状态码: {response.status_code}),"
                      f"地址或参数有误, 无需重试")
                print(f"  响应内容: {response.text[:200]}")
                return None

            # ===== 2xx 成功：解析 JSON 返回 =====
            if 200 <= response.status_code <300:
                return response.json()

            # ===== 5xx 服务器错误：记录后进入重试 =====
            last_error = f"服务器错误 (状态码: {response.status_code})"
            print(f"{last_error}, 第 {retry} 次重试...")

        except requests.exceptions.Timeout:
            last_error = "请求超时"
            print(f"请求超时, 第 {retry} 次重试...")

        except requests.exceptions.ConnectionError:
            last_error = "连接失败"
            print(f"连接失败, 第 {retry} 次重试...")

        except Exception as e:
            last_error = f"未知错误: {e}"
            print(f"{last_error}, 第 {retry} 次重试...")

        # ===== 指数退避：第1次等1秒，第2次等2秒，第3次等4秒 =====
        # 最后一次失败后不再等待
        if retry < max_retries:
            delay = 2 ** (retry - 1)
            time.sleep(delay)

    # ===== 重试耗尽，仍然失败 =====
    print(f"重试 {max_retries} 次后仍然失败: {last_error}")
    return None