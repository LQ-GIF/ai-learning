"""入口层：命令行交互"""

import argparse
from models import search_cases
from data_loader import export_result

def create_parser():
    parser = argparse.ArgumentParser(description="建筑案例搜索工具 v1.0")
    parser.add_argument("--keyword", help="按关键词搜索案例名")
    parser.add_argument("--city", help="按城市筛选, 如: 杭州")
    parser.add_argument("--type", help="按类型筛选: 商业/文化/住宅/教育/办公")
    parser.add_argument("--min-area", type=int, help="最小面积(㎡)")
    parser.add_argument("--export", help="导出结果到指定CSV文件, 如: --export result.csv")
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    if not any([args.keyword, args.city, args.type, args.min_area, args.export]):
        parser.print_help()
        return

    results = search_cases(
        keyword=args.keyword,
        city=args.city,
        case_type=args.type,
        min_area=args.min_area
    )

    print(f"\n找到 {len(results)} 个案例: ")
    print("-" * 60)
    for i, c in enumerate(results, 1):
        print(f"{[i]} {c['案例名']} | {c['城市']} | {c['类型']} | {c['面积']}㎡")
    print("-" * 60)

    if args.export:
        export_result(results, args.export)

if __name__ == "__main__":
    main()