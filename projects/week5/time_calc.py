"""
时间计算工具
1. 格式化输出当前时间
2. 计算距离 2027年6月1日毕业还有多少天
3. 演示时间戳和 datetime 的区别
"""

from datetime import datetime, date

# ========== 第 1 步：获取当前时间 ==========
now = datetime.now()
print("=" * 50)
print("【当前时间】")
print(f"原始格式 (电脑内部) : {now}")
print(f"格式化输出: {now.strftime('%Y年%m月%d日 %H:%M:%S')}")
print(f"只要日期: {now.strftime('%Y-%m-%d')} \n          {now.strftime('%Y/%m/%d')}")
print(f"只要时间: {now.strftime('%H:%M:%S')} \n          {now.strftime('%H时%M分%S秒')}")
print(f"中文日期: {now.strftime('%Y年%m月%d日')}")
print(f"星期: {now.strftime('%A')}")

# ========== 第 2 步：造一个"毕业日" ==========
# datetime(年, 月, 日) 就能造出一个指定日期
graduation = datetime(2027, 7, 1)
print("\n" + "=" * 50)
print("【毕业日】")
print(f"毕业日期: {graduation.strftime('%Y年%m月%d日')}")

# ========== 第 3 步：算时间差 ==========
# 两个 datetime 相减，得到一个 timedelta 对象
diff = graduation - now
print("=" * 50)
print("【倒计时】")
print(f"距离毕业还有: {diff.days} 天")
print(f"精确到秒: {diff.total_seconds():.0f} 秒")

# ========== 第 4 步：时间戳 vs datetime ==========
print("\n" + "=" * 50)
print("【时间戳演示】")
timestamp = now.timestamp()
print(f"当前时间戳 (数字) : {timestamp:.0f}")
print(f"时间戳换回去: {datetime.fromtimestamp(timestamp)}")
print()
print("时间戳就是从 1970-01-01 00:00:00 到现在过了多少秒。")
