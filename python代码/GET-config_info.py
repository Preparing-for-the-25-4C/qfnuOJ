import requests

# 假设你已知道主机上映射的端口（例如：32769），你可以通过运行 'docker ps' 来查找它
# 如果没有指定，Docker会随机分配一个端口，你需要找到它
host_port = 2358  # 替换为实际映射到2358的端口

# 设置API的URL和IP，使用正确的端口
api_url = f"http://192.168.131.138:{host_port}/config_info"

# 发送GET请求来获取配置信息
response = requests.get(api_url)

# 检查响应状态
if response.status_code == 200:
    # 打印配置信息
    config_info = response.json()
    for key, value in config_info.items():
        print(f"{key}: {value}")
else:
    # 打印错误信息
    print(f"Failed to get config info. Status code: {response.status_code}")
    print(response.text)
