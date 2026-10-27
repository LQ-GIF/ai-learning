import json
import os
import logging
from typing import List, Dict, Any

# ========== 日志配置 ==========
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("projects/week4/shopping_cart.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

DATA_FILE = "projects/week4/shopping_list.json"
mailing_area = ["山西", "四川", "贵州", "浙江", "深圳"]
shipping_fee = {"山西": 5, "四川": 10, "贵州": 8, "浙江": 15, "深圳":11}

# ========== 商品清单加载和保存 ==========
# ========== 商品清单加载 ==========
def load_product():
    if not os.path.exists(DATA_FILE):
        logging.warning(f"商品清单{DATA_FILE}不存在, 将创建新清单")
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            products = json.load(f)
        logging.info(f"成功加载 {len(products)} 件商品")
        return products
    except json.JSONDecodeError:
        logging.error(f"商品清单{DATA_FILE}格式损坏, 将返回空清单")
        return []
    except Exception as e:
        logging.error(f"商品清单出现未知错误, 错误信息为: {e}")
        return []

# ========== 商品清单保存 ==========
def save_product(products: List[Dict]) -> Any:
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(products, f, ensure_ascii=False, indent=2)
        logging.info(f"成功保存 {len(products)} 件商品")
        return True
    except PermissionError:
        logging.error(f"保存失败, 没有文件{DATA_FILE}的写入权限")
        return False
    except Exception as e:
        logging.error(f"保存商品时发生未知错误, 错误信息为: {e}")
        return False

# ========== 商品操作函数 ==========
# ========== 添加商品 ==========
def add_product(products: List[Dict]) -> List[Dict]:
    print("\n--- 添加商品 ---")
    name: str = input("请输入商品名称: ").strip()
    if not name:
        print("商品名称不能为空")
        logging.warning("商品添加失败, 商品名称为空")
        return products
    else:
        try:
            quantity: int = int(input("请输入商品数量: ").strip())
            price: float = float(input("请输入商品价格: ").strip())
            mailing_address: str = input("请输入邮寄地址: ").strip()
        except ValueError:
            logging.error("输入数据格式错误")
            print("输入数据格式错误, 请按规则重新输入!!!")
            return products

    product: Dict = {
        "商品名称": name,
        "商品数量": quantity,
        "商品价格": price,
        "邮寄地址": mailing_address
    }

    products.append(product)
    logging.info(f"添加了新商品{name}")
    print(f"商品{name}添加成功")
    save_product(products)
    return products

# ========== 查看所有添加的商品 ==========
def list_product(products: List[Dict]) -> str:
    print("\n--- 商品清单 ---")
    if not products:
        print("暂无商品！！！")
        return
    else:
        for i, product in enumerate(products, 1):
            print(f"[{i}] {product['商品名称']} | 商品数量：{product['商品数量']} | 商品价格：{product['商品价格']} | 邮寄地址：{product['邮寄地址']} ")

# ========== 搜索已添加的商品 ==========
def search_product(products: List[Dict]) -> str:
    print("\n--- 搜索商品 ---")
    keyword: str = input("请输入要搜索的商品名称关键词: ").strip()
    if not keyword:
        logging.info("搜索失败: 关键词为空!!!")
        print("搜索关键词不能为空！")
        return
    else:
        found = False
        for i, product in enumerate(products, 1):
            if keyword in product['商品名称']:
                print(f"找到商品（序号[{i}]")
                print(f"  商品名称：{product['商品名称']}")
                print(f"  商品数量：{product['商品数量']}")
                print(f"  商品价格：{product['商品价格']}")
                print(f"  邮寄地址：{product['邮寄地址']}")
                found = True
        if not found:
            print(f"未找到包含「{keyword}」的商品。")
            logging.info(f"搜索「{keyword}」：未找到相关商品")
        else:
            logging.info(f"搜索「{keyword}」：找到相关商品")

# ========== 删除已添加的商品 ==========
def deleted_product(products: List[Dict]) -> List[Dict]:
    print("\n--- 删除商品 ---")
    if not products:
        print("暂无商品数据，无法删除。")
        return products
    else:
        list_product(products)
        choice: int = int(input("请输入要删除的商品序号: ").strip())

        try:
            index = choice - 1
            if index < 0 or index >= len(products):
                print("序号超出范围！")
                logging.warning(f"删除商品失败, 序号{choice}超出范围")
                return products
            else:
                deleted_name = products[index]['商品名称']
                products.pop(index)
                logging.info(f"删除了商品：{deleted_name} (序号{choice})")
                print(f"商品「{deleted_name}」删除成功！")
                save_product(products)
                return products
        except ValueError:
            print("输入错误！请输入一个有效的数字序号。")
            logging.warning(f"删除商品失败：输入「{choice}」不是有效数字")
            return products

# ========== 计算商品运费 ==========
def calculate_shipping(products: List[Dict]) -> float:
    print("\n--- 计算运费 ---")

    total = 0

    for product in products:
        if product['邮寄地址'] in mailing_area:
            print(f"{product['邮寄地址']} 在配送地区内, 正在计算运费")
            print(shipping_fee.get(product['邮寄地址']) * 2)
            total += shipping_fee.get(product['邮寄地址']) * 2
        elif not product['邮寄地址']:
            print("邮寄地址为空, 请输入邮寄地址")
        else:
            print(f"{product['邮寄地址']} 不在配送地区内，请修改配送地址")

    print(f"运费总金额为{total}元")
    return total
    

# ========== 计算商品总价 ==========
def total_price(products: List[Dict]) -> float:
    print("\n--- 计算总价 ---")
    if not products:
        print("暂无商品数据，无法计算总价。")
        return products
    else:
        list_product(products)
        total = 0
        for product in products:
            if product['邮寄地址'] in mailing_area:
                print(f"商品{product['商品名称']}的价格为 {product['商品数量'] * product['商品价格']} 元")
                total += product['商品数量'] * product['商品价格']
            else:
                print("-" * 65)
                print(f"商品{product['商品名称']}的价格为 {product['商品数量'] * product['商品价格']} 元")
                print("该商品邮寄地址不在可配送区域内, 请重新选择邮寄地址")

        total_calculate_shipping = calculate_shipping(products)
        total_prices = total + total_calculate_shipping
        print(f"商品总金额为{total_prices}元")
        return total_prices


# ========== 主程序 ==========
def main():
    logging.info("购物车管理系统启动")
    products = load_product()

    while True:
        print("\n" + "=" * 40)
        print("  购物车管理系统")
        print("  1. 添加商品")
        print("  2. 查看所有商品")
        print("  3. 搜索商品")
        print("  4. 删除商品")
        print("  5. 计算总运费")
        print("  6. 计算总价(含运费)")
        print("  7. 保存并退出")
        print("=" * 40)

        try:
            choice = int(input("请输入选项 (1 - 7): ").strip())
            option = choice
        except ValueError:
            print("输入错误！请输入 1-7 之间的数字。")
            logging.warning(f"菜单输入错误：「{choice}」不是有效数字")
            continue

        if option == 1:
            products = add_product(products)
        elif option == 2:
            list_product(products)
        elif option == 3:
            search_product(products)
        elif option == 4:
            deleted_product(products)
        elif option == 5:
            calculate_shipping(products)
        elif option == 6:
            total_price(products)
        elif option == 7:
            if save_product(products):
                print("商品数据已保存，再见！")
                logging.info("购物车管理系统正常退出")
            else:
                print("数据保存失败，但程序仍将退出。请检查日志文件了解详情。")
                logging.error("程序退出时数据保存失败")
            break
        else:
            print("选项超出范围！请输入 1-7 之间的数字。")
            logging.warning(f"菜单输入错误：选项 {option} 超出范围")

if __name__ == "__main__":
    main()