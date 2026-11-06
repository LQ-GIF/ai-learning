"""业务层：筛选逻辑"""

from data import cases

def search_cases(keyword=None, city=None, case_type=None, min_area=None):
    resules = cases

    if keyword:
        resules = [c for c in resules if keyword in c['name']]

    if city:
        resules = [c for c in resules if city == c['city']]

    if case_type:
        resules = [c for c in resules if case_type == c['type']]

    if min_area:
        resules = [c for c in resules if min_area <= c['area']]
    
    return resules