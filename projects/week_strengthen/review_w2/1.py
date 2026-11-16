cases = [
    {"name": "A", "area": 800},
    {"name": "B", "area": 1200},
    {"name": "C", "area": 350},
]

result = sorted(cases, key=lambda c: c["area"], reverse=True)


print([c["name"] for c in result])
