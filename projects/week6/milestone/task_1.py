import json
FILE = "cases.json"
PATH = "cases_hz.json"
city = "杭州"

def load_case(input_file):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            return json.load(f)
            
    except FileNotFoundError:
        print("文件不存在")
        return None
    except json.JSONDecodeError:
        print("JSON 文件格式错误")
        return None
    except Exception as e:
        print(f"未知错误, 错误信息为: {e}")
        return None

def filter_case(load_result, keys):
    cases_result = [c for c in load_result if c['city'] == keys]
    return cases_result

def dump_case(filter_result, output_file):
    with open(output_file, "w", encoding="utf-8") as k:
        json.dump(filter_result, k, ensure_ascii=False, indent=2)



if __name__ == "__main__":
    data = load_case(FILE)
    if data is None:
        print("无法读取")
    else:
        cases_hz = filter_case(data, city)
        if len(cases_hz) == 0:
            print("筛选结果为空, 不进行写入操作")
        else:
            dump_case(cases_hz, PATH)
        print(f"共读取 {len(data)} 条案例, 筛选出 {city} 的案例有 {len(cases_hz)} 条")

