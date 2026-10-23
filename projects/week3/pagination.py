# 导入需要的库
import os
import requests
import json
import time
from dotenv import load_dotenv

# 加载 .env 文件（今天虽然不用鉴权，但养成习惯，以后写代码统一加载）
load_dotenv()

# ===== 配置信息 =====
GITHUB_USER = "torvalds"                # 要获取仓库的 GitHub 用户名
BASE_URL = f"https://api.github.com/users/{GITHUB_USER}/repos"
PER_PAGE = 10                           # 每页多少条
MAX_RETRIES = 3                         # 最多重试次数
RETRY_DELAY = 3                         # 重试间隔（秒）
SLEEP_BETWEEN_PAGES = 1                 # 每页之间限速等待（秒）

# 存放所有仓库的列表
all_repos = []
# 当前页码，从第1页开始
page = 1
# 记录已经重试了多少次
total_retry_count = 0

print("=" * 50)
print(f"开始获取 GitHub 用户 {GITHUB_USER} 的所有仓库")
print(f"每页 {PER_PAGE} 条, 最多重试 {MAX_RETRIES}次")
print("=" * 50)

# ===== 分页循环 =====
while True:
    print(f"正在获取第 {page} 页")

    # 重试计数器
    retry_count = 0
    response = None
    success = False

    # ===== 重试逻辑 =====
    while retry_count < MAX_RETRIES:
        try:
            params = {"page": page, "per_page": PER_PAGE, "sort": "updated"}
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(BASE_URL, params=params, headers=headers, timeout=10)

            # 状态码 200 = 成功
            if response.status_code == 200:
                success = True
                break
            # 状态码为4xx，直接提示错误，不重试
            elif 400 <= response.status_code < 500:
                print(f"  请求被拒绝 (状态码: {response.status_code}), 地址或参数有误, 无需重试")
                print(f"响应内容: {response.text}")
                success = False
                break
            # 状态码不是200，打印信息并重试
            else:
                retry_count += 1
                total_retry_count += 1
                print(f"  ⚠️ 状态码 {response.status_code}, 第 {retry_count} 次重试...")
                time.sleep(RETRY_DELAY)
        except requests.exceptions.Timeout:
            retry_count += 1
            total_retry_count += 1
            print(f"  ⚠️ 请求超时，第 {retry_count} 次重试...")
            time.sleep(RETRY_DELAY)
        except requests.exceptions.ConnectionError:
            retry_count += 1
            total_retry_count += 1
            print(f"  ⚠️ 连接失败，第 {retry_count} 次重试...")
            time.sleep(RETRY_DELAY)
        except Exception as e:
            retry_count += 1
            total_retry_count += 1
            print(f"  未知错误: {e}, 第 {retry_count} 次重试...")
            time.sleep(RETRY_DELAY)

    # ===== 判断是否重试成功 ====
    if not success:
        print(f"  第 {page} 页重试 {MAX_RETRIES} 次后仍然失败, 停止获取")
        break

    # 解析这一页的仓库数据
    repos_page = response.json()

    # 如果这一页是空列表，说明没有更多数据了，跳出循环
    if len(repos_page) == 0:
        print(f"  第 {page} 页返回空列表, 没有更多仓库了")
        break

    # 把这一页的仓库添加到总列表里（extend 是把列表里的元素逐个加进去，不是把列表本身塞进去）
    all_repos.extend(repos_page)
    print(f"    第 {page} 页获取成功, 本页 {len(repos_page)} 个仓库, 累计 {len(all_repos)} 个仓库")
    # 限速：获取完这一页后等一下，再获取下一页
    time.sleep(SLEEP_BETWEEN_PAGES)
    # 页码 +1
    page += 1

# ===== 汇总结果 =====
print("\n" + "=" * 50)
print("获取完成! 统计结果: ")
print(f"  用户: {GITHUB_USER}")
print(f"  仓库总数: {len(all_repos)} 个")
print(f"  总页数: {page - 1} 页")
print(f"  重试总次数: {total_retry_count}")
print("=" * 50)

# ===== 保存为 JSON 文件 =====
output_path = os.path.join(os.path.dirname(__file__), "repos.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_repos, f, ensure_ascii=False, indent=2)
print(f"所有仓库数据已保存到: {output_path}")

# ===== 打印前5个仓库名称，验证结果 =====
print("\n前 5 个仓库：")
for i, repo in enumerate(all_repos[:5], 1):
    print(f"{i} {repo['name']} (星数: {repo['stargazers_count']})")

# 如果仓库超过5个，打印最后一个
if len(all_repos) > 5:
    print(f".....共 {len(all_repos)} 个仓库, 省略其他 {len(all_repos) - 5} 个仓库")


print("__file__ 的值：", __file__)
print("脚本所在文件夹：", os.path.dirname(__file__))
print("拼接后的输出路径：", os.path.join(os.path.dirname(__file__), "repos.json"))