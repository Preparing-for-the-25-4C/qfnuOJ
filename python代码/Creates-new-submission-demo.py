import requests
import base64

# API的URL
url = "http://192.168.131.138:2358/submissions"

# 示例代码，不需要Base64编码
data = {
    "source_code": "#include <stdio.h>\n\nint main(void) {\n  char name[10];\n  scanf(\"%s\", name);\n  printf(\"hello, %s\\n\", name);\n  return 0;\n}",
    "language_id": 49,
    "stdin": "world",
    "expected_output": "hello, world"
}

# 发送请求，不等待结果
response = requests.post(url, json=data)
print(response.status_code)
print(response.json())

# 示例代码，需要Base64编码
source_code_base64 = base64.b64encode(data['source_code'].encode()).decode()
stdin_base64 = base64.b64encode(data['stdin'].encode()).decode()
expected_output_base64 = base64.b64encode(data['expected_output'].encode()).decode()

data_base64 = {
    "source_code": source_code_base64,
    "language_id": 49,
    "stdin": stdin_base64,
    "expected_output": expected_output_base64,
    "base64_encoded": True
}

# 发送请求，使用Base64编码的数据
response_base64 = requests.post(url, json=data_base64)
print(response_base64.status_code)
print(response_base64.json())

# 示例代码，发送请求并等待结果
data_wait = {
    "source_code": "#include <stdio.h>\n\nint main(void) {\n  char name[10];\n  scanf(\"%s\", name);\n  printf(\"hello, %s\\n\", name);\n  return 0;\n}",
    "language_id": 49,
    "stdin": "Judge0",
    "expected_output": "hello, Judge0",
    "wait": True
}

# 发送请求，等待结果
response_wait = requests.post(url, json=data_wait)
print(response_wait.status_code)
print(response_wait.json())
