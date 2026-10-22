import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

print("=" * 50)
print("API 鉴权测试")
print("=" * 50)

if not api_key:
    print("❌ 错误：未能读取到 API Key!")
    print("请检查")
    print("  1. .env 文件是否存在于项目根目录")
    print("  2. .env 文件里是否有 API_KEY=xxx 这一行")
    print("  3. 键名是否拼写正确(API_KEY, 全大写)")
    exit()
else:
    print(f"✅ 成功读取 API Key: {api_key[:10]}...(已隐藏后半部分)")
    print(f"  Key 的长度: {len(api_key)}个字符")

url = "https://httpbin.org/headers"
headers = {
    "Authorization": f"Bearer {api_key}",
    "User-Agent": "Mozilla/5.0"
}

print("\n" + "=" * 50)
print("发送请求...")
print(f"URL: {url}")
print(f"请求头中的 Authorization: Bearer {api_key[:10]}...")
print("=" * 50)

try:
    response = requests.get(url, headers=headers, timeout=10)
    print(f"\n状态码: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print("\n" + "=" * 50)
        print(f"返回结果: {result}")
        print("\n" + "=" * 50)
        print("服务器返回的请求头")
        print("=" * 50)

        for key, value in result['headers'].items():
            print(f"{key}: {value}")

        print("\n" + "=" * 50)
        print("验证鉴权头: ")
        print("=" * 50)

        if "Authorization" in result['headers']:
            auth_header = result['headers']['Authorization']
            print("✅ Authorization 头已正确设置！")
            print(f"  完整值: {auth_header}")

            if auth_header.startswith("Bearer"):
                print("✅ 格式正确：以 'Bearer ' 开头")
                token_part = auth_header[7:]
                if token_part == api_key:
                    print(f"✅ Token 部分与 .env 文件中的 API Key 完全一致！")
                else:
                    print(f"❌ Token 部分与 API Key 不一致")
            else:
                print(f"❌ 格式错误：不是以 'Bearer ' 开头")
        else:
            print(f"❌ 未找到 Authorization 头！")
    else:
        print(f"\n请求失败, 状态码: {response.status_code}")
        print("错误信息:")
        print(response.text)
except requests.exceptions.Timeout:
    print("\n❌ 请求超时！网络不好或者服务器太慢，请检查网络后重试。")
except requests.exceptions.ConnectionError:
    print("\n❌ 连接失败！请检查网络连接。")
except Exception as e:
    print(f"\n❌ 发生未知错误: {e}")


# 额外练习：演示如果 API Key 错误会怎样
print("\n\n" + "=" * 50)
print("额外测试：如果用错误的 API Key 会怎样？")
print("=" * 50)

wrong_headers = {
    "Authorization": "Bearer wrong_key_12345",
    "User-Agent": "Mozilla/5.0"
}
try:
    wrong_response = requests.get(url, headers=wrong_headers, timeout=10)
    wrong_result = wrong_response.json()

    print(f"状态码: {response.status_code}")
    print("发送的错误 Key: wrong_key_12345")
    print(f"服务器收到的 Authorization: {wrong_result['headers'].get('Authorization', '未找到')}")
    print("\n💡 说明: httpbin 不会验证 Key 的真假，它只是原样返回请求头。")
    print("   真实的 API(比如大模型 API)会验证 Key, 如果 Key 错误会返回 401 未授权。")

except Exception as e:
    print(f"❌ 发生错误: {e}")
