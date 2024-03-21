import re
string = "0122923450321 王昊 法学1801 河北 2001年"
input_str = string.split()          # 替换成您要处理的字符串

name = input_str[1]
class_info = input_str[2]
print(f"姓名：{name}")
print(f"班级：{class_info}")

match = re.search(r'\d{4}', input_str[4])
if match:
    print(type(match))
    year = match.group()
    print(f"出生：{year}年")
else:
    print("未找到符合条件的年份")
