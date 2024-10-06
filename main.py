from script import convert_xml_to_json
import os

# 定义文件夹路径
directory_path = 'pro'

# 检查文件夹是否存在
if os.path.exists(directory_path):
    # 列出文件夹中的所有文件和文件夹
    entries = os.listdir(directory_path)

    # 过滤出所有文件（非文件夹）
    files = [entry for entry in entries if os.path.isfile(os.path.join(directory_path, entry))]
    a=1
    # 打印文件名
    for file in files:
        file="pro/"+file
        a=convert_xml_to_json(file,a)
        a+=1
else:
    print(f'文件夹 "{directory_path}" 不存在。')

# a=convert_xml_to_json('fps-ianwusb-27978,26967.xml',1)
# print(a)