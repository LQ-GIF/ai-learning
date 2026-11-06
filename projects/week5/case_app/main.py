"""入口层：命令行交互"""

import argparse
from models import search_cases

def create_parser():
    parser = argparse.ArgumentParser(description="建筑案例搜索工具")
    parser.add_argument("--keyword", help="按关键词搜索案例名")
    parser.add_argument("--city", help="按城市筛选案例")
    parser.add_argument("--type", help="按类型筛选案例")
    parser.add_argument("--min-area", type=int, help="最小面积")

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    if not any([args.keyword, args.city, args.type, args.min_area]):
        parser.print_help()
        return

    resules = search_cases(
        keyword=args.keyword,
        city=args.city,
        case_type=args.type,
        min_area=args.min_area
    )

    print(f"\n找到 {len(resules)} 个案例")
    print("-" * 60)
    for i, c in enumerate(resules, 1):
        print(f"{[i]}  {c['name']} | {c['city']} | {c['type']} | {c['area']}㎡")
    print("-" * 60)

if __name__ == "__main__":
    main()