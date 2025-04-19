import base64
import requests

# API的URL和提交令牌列表
url = "http://192.168.131.138:2358/submissions"
token_li = [
    'd35fc82b-bd1f-4ea9-93c9-105f8eb8d7e7',
    'cbd0dc7f-b576-4ad0-a5ad-712a22000aa6',
    'da85cb7b-0a8b-4d23-bb18-712c9f9b2fbf'
]

for token in token_li:
    # 获取特定字段的提交详情
    params = {
        "base64_encoded": False,
        "fields": "stdout,stderr,status_id,language_id"
    }

    # 发送请求
    response = requests.get(f"{url}/{token}", params=params)
    print(response.status_code)
    print(response.json())

    # 获取默认字段的提交详情
    response_default = requests.get(f"{url}/{token}")
    print(response_default.status_code)
    print(response_default.json())

    # 获取Base64编码的文本类型属性
    params_base64 = {
        "base64_encoded": True
    }

    # 发送请求以获取Base64编码的数据
    response_base64 = requests.get(f"{url}/{token}", params=params_base64)
    print(response_base64.status_code)
    response_data_base64 = response_base64.json()
    print(response_data_base64)

    # 如果需要，解码Base64编码的stdout
    if "stdout" in response_data_base64 and response_data_base64["stdout"] is not None:
        stdout_base64 = response_data_base64['stdout']
        stdout_decoded = base64.b64decode(stdout_base64).decode()
        print("Decoded stdout:", stdout_decoded)
    else:
        print("No stdout to decode or stdout is None")

    print()
# 200
# {'language_id': 49, 'stdout': 'hello, world\n', 'status_id': 3, 'stderr': None}
# 200
# {'stdout': 'hello, world\n', 'time': '0.004', 'memory': 14988, 'stderr': None, 'token': 'd35fc82b-bd1f-4ea9-93c9-105f8eb8d7e7', 'compile_output': None, 'message': None, 'status': {'id': 3, 'description': 'Accepted'}}
# 200
# {'stdout': 'hello, world\n', 'time': '0.004', 'memory': 14988, 'stderr': None, 'token': 'd35fc82b-bd1f-4ea9-93c9-105f8eb8d7e7', 'compile_output': None, 'message': None, 'status': {'id': 3, 'description': 'Accepted'}}
# Traceback (most recent call last):
#   File "D:\Develop\do\learn\code\python\PycharmProjects\pythonProject1\main.py", line 43, in <module>
#     stdout_decoded = base64.b64decode(stdout_base64).decode()
#                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Develop\ProgramFiles\anaconda3\Lib\base64.py", line 88, in b64decode
#     return binascii.a2b_base64(s, strict_mode=validate)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# binascii.Error: Incorrect padding