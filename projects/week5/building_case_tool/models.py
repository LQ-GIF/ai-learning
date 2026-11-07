"""业务层：筛选逻辑"""
from data_loader import load_case

def search_cases(keyword=None, city=None, case_type=None, min_area=None):
    cases = load_case()
    results = cases

    if keyword:
        results = [c for c in results if keyword in c['案例名']]

    if city:
        results = [c for c in results if city == c['城市']]

    if case_type:
        results = [c for c in results if case_type == c['类型']]

    if min_area:
        results = [c for c in results if min_area <= c['面积']]

    return results