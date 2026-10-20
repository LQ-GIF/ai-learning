import requests
url = "https://api.github.com/users/torvalds/repos"
param = {
    "page": 1,
    "per_page": 10,
    "sort": "update"
}
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, params=param, headers=headers, timeout=10)

# 打印状态码
print("=" * 50)
print(f"状态码: {response.status_code}")

print("=" * 50)
print(f"响应头: {response.headers}")
print("=" * 50)

try:
    if response.status_code == 200:
        repos = response.json()
        print(f"获取到{len(repos)}个仓库")
        print("=" * 50)

        for i, repo in enumerate(repos, 1):
            print(f"【仓库{i}】")
            print(f"名称: {repo['name']}")
            print(f"描述: {repo['description']}")
            print(f"星数: {repo['stargazers_count']}")
            print(f"语言: {repo['language']}")
            print(f"最后更新:{repo['updated_at']}")
            print("-" * 50)

        # 额外练习：找出星数最多的仓库
        print("\n" + "=" * 50)
        print("星数最多的仓库:")
        most_starred = max(repos, key=lambda r: r['stargazers_count'])
        print(f"{most_starred['name']} - {most_starred['stargazers_count']}星")
        print("=" * 50)
    else:
        print(f"请求失败, 状态码: {response.status_code}")
        print("信息错误")
        print(response.text)
except Exception as e:
    print(f"未知错误: {e}")