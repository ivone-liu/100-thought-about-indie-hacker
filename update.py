import os
import re

# 设置目录路径
opus_dir = './opus'
readme_path = './README.md'

# 获取 opus 目录中的所有 .md 文件
md_files = [f for f in os.listdir(opus_dir) if f.endswith('.md')]

# 提取文件名中的数字部分进行排序
def get_file_number(file_name):
    match = re.match(r'(\d+)', file_name)  # 匹配文件名中的数字部分
    if match:
        return int(match.group(1))  # 返回匹配到的数字部分
    return float('inf')  # 如果没有数字部分，返回一个极大的数字，确保它排在最后

# 按照文件名的数字部分进行排序
md_files.sort(key=get_file_number)

# 生成文件索引内容
index_content = '# Opus 目录文件索引\n\n'
for file in md_files:
    index_content += f'- [{file}](./opus/{file})\n'

# 读取现有的 README.md 内容
try:
    with open(readme_path, 'r', encoding='utf-8') as file:
        readme_content = file.read()
except FileNotFoundError:
    readme_content = ''

# 将索引插入到 README.md 的开头
updated_readme = index_content + '\n' + readme_content

# 写回更新后的 README.md
with open(readme_path, 'w', encoding='utf-8') as file:
    file.write(updated_readme)

print('README.md 已更新！')
