# **qfnuoj技术文档**

## 	一.技术栈和生产工具

### 		前端

框架：**Vue3**   **Axios**

Vue3常用组件库：
Vant 3.0   有赞前端团队开源的移动端组件库
**​Element Plus**   一套为开发者、设计师和产品经理准备的基于 Vue 3.0 的桌面端组件库
​Ant-design-vue   是 Ant Design 的 Vue 实现，组件的风格与 Ant Design 保持同步
​Naive UI   一个 Vue 3 组件库，比较完整，主题可调，使用 TypeScript，不算太慢,有点意思
​**Quasar**   构建高性能的 VueJS 用户界面,开箱即用,支持桌面和移动浏览器（包括 iOS Safari！）
​Arco Design Vue   字节跳动基于 Arco Design 开源的 Vue UI 组件
​Element3   一套Element风格，为开发者、设计师和产品经理准备的基于 Vue 3.0 的桌面端组件
​Varlet   基于 Vue3 的 Material design 风格移动端组件库
​Vue-devui   基于 DevUI Design 的 Vue3 组件库，使用 pnpm + vite + vue3 + tsx 技术搭建
​Idux   一个基于 Vue 3.x 和 TypeScript 开发的开源组件库
​NutUI 3   京东风格的 Vue 移动端组件库，开发和服务于移动Web界面的企业级产品

知识图谱框架：**SimpleMindMap** https://wanglin2.github.io/mind-map-docs/
代码编辑器: **Monaco Editor** https://wf0.github.io/api.html

### 		后端

框架：**SpringBoot3.4.0**    **Mybatis**   **JDK17**
缓存：**Redis7**
数据库：**MySql5.7**
前端服务器：**Nginx**
后端服务器：**Tomcat10**
操作系统：**Ubuntu22.04**
测评机：**Judge0**

### 		生产工具

Apifox：接口管理
Git/Github：项目版本管理

## 	二.架构设计

### 			系统架构

<img src="https://github.com/Preparing-for-the-25-4C/qfnuOJ/blob/%E6%8A%80%E6%9C%AF%E6%96%87%E6%A1%A3/qfnuoj%E7%B3%BB%E7%BB%9F%E6%9E%B6%E6%9E%84.png?raw=true" style="zoom: 50%;" />

### 	HTTP报文

**请求报文：**

请求头: 
```
Content-Type: application/json;charset=UTF-8
Authorization: 8fdc11c6-b261-499b-ac88-0b4623e77849
```
请求体:
json格式，按情况而定

**响应报文:**

响应头:
```
Content-Type: application/json;charset=UTF-8
Status-Code: 200
```
响应体:

```javascript
{
    "errCode": "xxxx", //根据业务自定义
    "data": {} //响应的具体数据
}
```

**PS：若需要上传或下载文件，具体参照Apifox**

**errCode列举:**
```
1000 业务正常
1001 服务器内部错误
1002 验证码错误
1003 用户名或密码错误
```

### 权限系统

RBAC权限系统：**token** + **redis**
具体内容参见：https://blog.csdn.net/m0_62006803/article/details/133962328?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522b3c44c363b3077ce56c14b90fd173f47%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=b3c44c363b3077ce56c14b90fd173f47&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-133962328-null-null.142^v100^pc_search_result_base8&utm_term=rbac%E6%9D%83%E9%99%90%E7%AE%A1%E7%90%86%E8%AE%BE%E8%AE%A1&spm=1018.2226.3001.4187

**权限标识**

```
system:problem:add
system:problem:update
system:problem:delete
system:problem:read

system:user:add
system:user:update
system:user:delete
system:user:read

system:role:add
system:role:update
system:role:delete
system:role:read

system:perm:add
system:perm:update
system:perm:delete
system:perm:read

超级权限：system
```

### 库表设计

参见qfnuoj.sql文件

## 三.接口设计

接口设计采用**RESTFUL**风格，参见：https://blog.csdn.net/weixin_45658814/article/details/130879975?ops_request_misc=%257B%2522request%255Fid%2522%253A%25220603cccec793f110bc247c63947a8543%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=0603cccec793f110bc247c63947a8543&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-2-130879975-null-null.142

接口文档的编写使用**Apifox**

## 四.前端设计
