"""删除Python代码中的注释"""
import re

def remove_comments(code):
    pattern = r"(\".*?\"|\'.*?\')|(#.*)"
    # 正则表达式，用于匹配双引号、单引号内的内容和注释
    code = re.sub(pattern, lambda x: x.group(1) or '', code)
    # 替换匹配到的内容，双引号、单引号内的内容保留，注释替换为空字符串
    return code

# 读取 Python 代码文件
with open("D:\Code\mobile_cla\model\CNN_cpu.py", "r",encoding='utf-8') as f:
    code = f.read()

# 删除注释
code_without_comments = remove_comments(code)

# 输出结果
print(code_without_comments)
