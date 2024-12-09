# Judge0配置文档

## 一.安装Docker和Docker Compose

### 1.安装Docker

#### （1）一键安装命令：

```
sudo curl -fsSL https://gitee.com/tech-shrimp/docker_installer/releases/download/latest/linux.sh| bash -s docker --mirror Aliyun
```

#### （2）启动docker

```
sudo service docker start
```

#### （3）配置镜像站

```
sudo vi /etc/docker/daemon.json
```

输入下列内容，最后按ESC，输入 :wq! 保存退出。

```
{
    "registry-mirrors": [
        "https://docker.m.daocloud.io",
        "https://docker.1panel.live",
        "https://hub.rat.dev"
    ]
}
```

重启docker

```
sudo service docker restart
```

### 2.Docker-Compose 安装

Linux 上我们可以从 Github 上下载它的二进制包来使用，最新发行的版本地址：https://github.com/docker/compose/releases。

#### 运行以下命令以下载 Docker Compose 的当前稳定版本：

```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.2.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

> Docker Compose 存放在 GitHub，不太稳定。
>
> 你可以也通过执行下面的命令，高速安装 Docker Compose。
>
> ```
> curl -L https://get.daocloud.io/docker/compose/releases/download/v2.4.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
> ```

#### 将可执行权限应用于二进制文件：

```
sudo chmod +x /usr/local/bin/docker-compose
```

#### 创建软链：

```
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

#### 测试是否安装成功：

```
docker-compose version
```

## 二.GRUB的更新

- 使用sudo打开文件/etc/default/grub

- 在GRUB_CMDLINE_LINUX变量的值中添加systemd.unified_cgroup_hierarchy=0。

- 应用更改：sudo update-grub

- 重启服务器：sudo reboot

## 三.部署

### 1.下载并解压发布档案

```
wget https://github.com/judge0/judge0/releases/download/v1.13.1/judge0-v1.13.1.zip
unzip judge0-v1.13.1.zip
```

### 2.拉取镜像

```
docker pull crpi-l7ij7p17lt67sp5y.cn-qingdao.personal.cr.aliyuncs.com/ianwusb-docker-images/postgres:16.2
docker pull crpi-l7ij7p17lt67sp5y.cn-qingdao.personal.cr.aliyuncs.com/ianwusb-docker-images/redis:7.2.4
```

拉完这两个存一下快照，接着拉下面的

```
docker pull crpi-l7ij7p17lt67sp5y.cn-qingdao.personal.cr.aliyuncs.com/ianwusb-docker-images/compilers
```

> ```
> crpi-l7ij7p17lt67sp5y.cn-qingdao.personal.cr.aliyuncs.com/ianwusb-docker-images/judge0:1.13.1
> ```

### 3.将 docker-compose.yml替换成下面的内容

可以更改端口映射

```yml
x-logging:
  &default-logging
  logging:
    driver: json-file
    options:
      max-size: 100M

services:
  server:
    image: crpi-l7ij7p17lt67sp5y.cn-qingdao.personal.cr.aliyuncs.com/ianwusb-docker-images/compilers
    volumes:
      - ./judge0.conf:/judge0.conf:ro
    ports:
      - "2358:2358"
    privileged: true
    <<: *default-logging
    restart: always

  workers:
    image: crpi-l7ij7p17lt67sp5y.cn-qingdao.personal.cr.aliyuncs.com/ianwusb-docker-images/compilers
    command: ["./scripts/workers"]
    volumes:
      - ./judge0.conf:/judge0.conf:ro
    privileged: true
    <<: *default-logging
    restart: always

  db:
    image: crpi-l7ij7p17lt67sp5y.cn-qingdao.personal.cr.aliyuncs.com/ianwusb-docker-images/postgres:16.2
    env_file: judge0.conf
    volumes:
      - data:/var/lib/postgresql/data/
    <<: *default-logging
    restart: always

  redis:
    image: crpi-l7ij7p17lt67sp5y.cn-qingdao.personal.cr.aliyuncs.com/ianwusb-docker-images/redis:7.2.4
    command: [
      "bash", "-c",
      'docker-entrypoint.sh --appendonly no --requirepass "$$REDIS_PASSWORD"'
    ]
    env_file: judge0.conf
    <<: *default-logging
    restart: always

volumes:
  data:
```

### 4.更改judge0.conf

访问[random.org/passwords/?num=1&len=32&format=plain&rnd=new](https://www.random.org/passwords/?num=1&len=32&format=plain&rnd=new)生成一个随机密码。
使用生成的密码更新judge0.conf文件中的REDIS_PASSWORD变量。
再次访问[random.org/passwords/?num=1&len=32&format=plain&rnd=new](https://www.random.org/passwords/?num=1&len=32&format=plain&rnd=new)生成另一个随机密码。
使用生成的密码更新judge0.conf文件中的POSTGRES_PASSWORD变量。

### 5.自定义judge0.conf文件，可根据分支中的【judge0(译文).txt】文件

### 6.运行所有服务，并等待几秒钟直到一切初始化完成：

```
cd judge0-v1.13.1
docker-compose up -d db redis
sleep 10s
docker-compose up -d
sleep 5s
```

> 文档默认地址：http://<您服务器的IP地址>:2358/docs
>

http://<您服务器的IP地址>:端口映射/docs

## 四.官方API文档

[Judge0 CE - API Docs](https://ce.judge0.com/docs)