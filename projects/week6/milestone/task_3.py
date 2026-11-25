import json
from datetime import datetime

class Case:
    def __init__(self, name, area, city, year):
        self.name = name
        self.area = area
        self.city = city
        self.year = year

    def introduction(self):
        return f"{self.name} 的面积为 {self.area} 平方米, 所在地是 {self.city}, 建成年份为 {self.year} 年"

    def case_year(self):
        total = datetime.now().year - self.year
        return f"到目前为止, {self.name} 一共建成 {total} 年"

    def to_dict(self):
        return {
            "name": self.name,
            "city": self.city,
            "area": self.area,
            "year": self.year
        }

    def save_case(self, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    path1 = "class1.json"
    path2 = "class2.json"
    path3 = "class3.json"
    
    c1 = Case("未来科技城研发楼", 5400, "杭州", 2020)
    c2 = Case("老厂房创意园", 7800, "杭州", 2016)
    c3 = Case("望京SOHO塔", 8900, "北京", 2014)
    print(f"{c1.introduction()}\n{c1.case_year()}")
    print(f"{c2.introduction()}\n{c2.case_year()}")
    print(f"{c3.introduction()}\n{c3.case_year()}")
    c1.save_case(path1)
    c2.save_case(path2)
    c3.save_case(path3)
