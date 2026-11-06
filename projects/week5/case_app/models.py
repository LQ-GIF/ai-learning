"""业务层：筛选逻辑"""

from data import cases

def search_cases(keyword=None, city=None, case_type=None, min_area=None):
    results = cases

    if keyword:
        results = [c for c in results if keyword in c['name']]

    if city:
        results = [c for c in results if city == c['city']]

    if case_type:
        results = [c for c in results if case_type == c['type']]

    if min_area:
        results = [c for c in results if min_area <= c['area']]
    
    return results