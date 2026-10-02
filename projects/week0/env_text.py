from dotenv import load_dotenv
import os
load_dotenv()
demo_key = os.getenv("DEMO_KEY")
print("从.env文件里读取到的 DEMO_KEY 是：")
print(demo_key)
not_demo_key = os.getenv("NOT_DEMO_KEY")
print("读取一个不存在的变量,结果是：")
print(not_demo_key)