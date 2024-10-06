import xml.etree.ElementTree as ET
import json
import re

def convert_xml_to_json(file_path, start_id=1):
    # 解析XML文件
    tree = ET.parse(file_path)
    root = tree.getroot()

    # 初始化id计数器
    id_counter = start_id

    # 将XML转换为字典
    def xml_to_dict(element):
        nonlocal id_counter  # 使用非局部变量id_counter
        node = {}
        if element.text and element.text.strip():
            text_with_images_replaced = re.sub(r'<img.*?>', '&&缺少图片...&&', element.text.strip())
            node['text'] = re.sub(r'<[^>]+>', '', text_with_images_replaced)

        for attr, value in element.attrib.items():
            node['@' + attr] = value

        if element.tag == 'item':
            node['id'] = f"{id_counter:08d}"
            id_counter += 1

        for child in element:
            child_data = xml_to_dict(child)
            if child.tag in node:
                if not isinstance(node[child.tag], list):
                    node[child.tag] = [node[child.tag]]
                node[child.tag].append(child_data)
            else:
                node[child.tag] = child_data
        return node

    xml_dict = xml_to_dict(root)

    keys_to_remove = ["@version", "@url", "generator"]
    for key in keys_to_remove:
        if key in xml_dict:
            del xml_dict[key]

    json_data = json.dumps(xml_dict, indent=4, ensure_ascii=False)

    output_json_file_path = f'json/{start_id}-{id_counter-1}.json'
    with open(output_json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

    print(f"修改后的JSON数据已保存到{output_json_file_path}，最后一项的ID为：{(id_counter - 1):08d}")
    return id_counter - 1

# 使用函数并传入文件路径和开始ID
# last_item_id = convert_xml_to_json('fps-ianwusb-27978,26967.xml', 1)