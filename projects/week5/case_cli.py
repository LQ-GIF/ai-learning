"""
建筑案例命令行搜索工具
用法：
  python case_cli.py --keyword 咖啡馆
  python case_cli.py --city 杭州
  python case_cli.py --type 商业 --min-area 200
  python case_cli.py --help
"""

import argparse

# ========== 内置案例数据 ==========
cases = [
    {"name": "西湖边现代咖啡馆", "city": "杭州", "type": "商业", "area": 150},
    {"name": "西溪湿地图书馆", "city": "杭州", "type": "文化", "area": 800},
    {"name": "上海外滩美术馆", "city": "上海", "type": "文化", "area": 1200},
    {"name": "南京新中式别墅", "city": "南京", "type": "住宅", "area": 350},
    {"name": "杭州未来幼儿园", "city": "杭州", "type": "教育", "area": 600},
    {"name": "上海工业风书店", "city": "上海", "type": "商业", "area": 200},
    {"name": "苏州复古餐厅", "city": "苏州", "type": "商业", "area": 280},
    {"name": "杭州极简办公楼", "city": "杭州", "type": "办公", "area": 2000},
]

# ========== 第 1 步：定义命令行参数 ==========
def create_parser():
    parser = argparse.ArgumentParser(description="建筑案例搜索工具")
    # --keyword：按关键词搜案例名
    parser.add_argument("--keyword", help="按关键字搜索案例名, 例: 咖啡馆")
    # --city：按城市筛选
    parser.add_argument("--city", help="按城市筛选案例, 例: 杭州")
    # --type：按类型筛选
    parser.add_argument("--type", help="按类型筛选案例: 住宅/商业/文化/教育/办公")
    # --min-area：最小面积
    parser.add_argument("--min-area", type=int, help="最小面积 (整数) ")
    return parser

# ========== 第 2 步：筛选逻辑 ==========
def search_cases(keyword=None, city=None, case_type=None, min_area=None):
    results = cases

    # 关键词筛选
    if keyword:
        results = [c for c in results if keyword in c['name']]

    # 城市筛选
    if city:
        results = [c for c in results if city == c['city']]

    # 类型筛选
    if case_type:
        results = [c for c in results if case_type == c['type']]

    # 面积筛选
    if min_area:
        results = [c for c in results if min_area <= c['area']]

    return results

# ========== 第 3 步：主流程 ==========
def main():
    parser = create_parser()
    args = parser.parse_args()

    # 如果什么参数都没给，提示用法
    if not any([args.keyword, args.city, args.type, args.min_area]):
        parser.print_help()
        return

    results = search_cases(
        keyword=args.keyword,
        city=args.city,
        case_type=args.type,
        min_area=args.min_area
    )

    print(f"找到 {len(results)} 个案例: ")
    print("-" * 60)
    for i, c in enumerate(results, 1):
        print(f"{[i]} {c['name']} | {c['city']} | {c['type']} | {c['area']}㎡")
    print("-" * 60)

if __name__ == "__main__":
    main()