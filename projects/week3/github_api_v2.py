"""
github_api_v2.py - 使用封装好的 api_utils 调用 GitHub API 获取仓库列表

对比 github_api.py (Day2 原版):
本文件不再重复写状态码判断、重试、异常捕获，全部由 api_call 统一处理。
"""

from api_utils import api_call

def main():
    username = "torvalds"
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"User-Agent": "Mozilla/5.0"}

    print("=" * 50)
    print(f"开始获取 GitHub 用户 {username} 的仓库列表")
    print("=" * 50)

    # 一行调用完成：发请求 + 状态码判断 + 重试 + 异常处理 + JSON 解析
    repos = api_call(
        method="get",
        url=url,
        params={"per_page": 10, "sort": "updated"},
        headers=headers
    )

    # 工具函数失败时返回 None，必须先判断再使用结果
    if repos is None:
        print("\n获取失败, 程序结束")
        return

    print(f"成功获取 {len(repos)} 个仓库:")
    for i, repo in enumerate(repos, 1):
        print(f"[{i}] {repo['name']} (星数: {repo['stargazers_count']})")

# 脚本直接运行时执行 main()；被别的文件导入时不自动执行
if __name__ == "__main__":
    main()