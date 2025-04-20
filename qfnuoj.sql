-- qfnuoj库表设计
-- 表：用户，用户角色，角色，角色权限，权限，题目，
-- 用户题目，登录日志，操作日志，测评记录，异常日志，
-- 题目补充信息，排名

CREATE TABLE `user` (
  `user_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '用户ID',
  `user_name` VARCHAR (20) NOT NULL UNIQUE COMMENT '用户名',
  `user_password` CHAR(32) NOT NULL COMMENT '密码(使用md5算法加密)',
  `user_sex` CHAR(1) NOT NULL DEFAULT '2' COMMENT '性别(0表示女性,1表示男性,2表示未知)',
  `user_phone` CHAR(11) NOT NULL DEFAULT '' UNIQUE COMMENT '中国大陆手机号',
  `user_email` VARCHAR (100) NOT NULL DEFAULT '' UNIQUE COMMENT '电子邮箱',
  `user_profile` VARCHAR (100) NOT NULL DEFAULT '' COMMENT '头像地址',
  `user_school` VARCHAR (100) NOT NULL DEFAULT '' COMMENT '用户学校',
  `del_flag` CHAR(1) NOT NULL DEFAULT '0' COMMENT '删除标记(0表示可用,1表示删除)',
  `create_by` VARCHAR (20) NOT NULL COMMENT '创建者用户名',
  `create_time` DATETIME NOT NULL COMMENT '创建时间',
  `update_by` VARCHAR (20) NOT NULL COMMENT '修改者用户名',
`update_time` DATETIME NOT NULL COMMENT '修改时间') ENGINE = INNODB COMMENT = '用户表';

CREATE TABLE `role` (
  `role_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '角色ID',
  `role_name` VARCHAR (20) NOT NULL UNIQUE COMMENT '角色名',
  `del_flag` CHAR(1) NOT NULL DEFAULT '0' COMMENT '删除标记(0表示可用,1表示删除)',
  `create_by` VARCHAR (20) NOT NULL COMMENT '创建者用户名',
  `create_time` DATETIME NOT NULL COMMENT '创建时间',
  `update_by` VARCHAR (20) NOT NULL COMMENT '修改者用户名',
`update_time` DATETIME NOT NULL COMMENT '修改时间') ENGINE = INNODB COMMENT = '角色表';
CREATE TABLE `user_role` (`user_id` INT NOT NULL COMMENT '用户ID', `role_id` INT NOT NULL COMMENT '角色ID') ENGINE = INNODB COMMENT = '用户角色表';

CREATE TABLE `perm` (
  `perm_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '权限ID',
  `perm_tag` VARCHAR (100) NOT NULL UNIQUE COMMENT '权限标识',
  `del_flag` CHAR(1) NOT NULL DEFAULT '0' COMMENT '删除标记(0表示可用,1表示删除)',
  `create_by` VARCHAR (20) NOT NULL COMMENT '创建者用户名',
  `create_time` DATETIME NOT NULL COMMENT '创建时间',
  `update_by` VARCHAR (20) NOT NULL COMMENT '修改者用户名',
`update_time` DATETIME NOT NULL COMMENT '修改时间') ENGINE = INNODB COMMENT = '权限表';
CREATE TABLE `role_perm` (`role_id` INT NOT NULL COMMENT '角色ID', `perm_id` INT NOT NULL COMMENT '权限ID') ENGINE = INNODB COMMENT = '角色权限表';-- ALTER TABLE `prob` AUTO_INCREMENT = 1;

CREATE TABLE `prob` (
  `prob_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '题目ID',
  `prob_title` VARCHAR (100) NOT NULL COMMENT '题目标题',
  `prob_content` LONGTEXT NOT NULL COMMENT '题目内容(最大支持4GB)',
  `prob_test` VARCHAR (100) NOT NULL COMMENT '测试数据地址',
  `del_flag` CHAR(1) NOT NULL DEFAULT '0' COMMENT '删除标记(0表示可用,1表示删除)',
  `prob_ac` INT NOT NULL DEFAULT 0 COMMENT '通过人数',
  `prob_commit` INT NOT NULL DEFAULT 0 COMMENT '尝试人数',
  `prob_success` DOUBLE NOT NULL DEFAULT 0 COMMENT '正确率',
  `prob_check` INT NOT NULL DEFAULT 0 COMMENT '点击量',
  `prob_origin` VARCHAR (100) NOT NULL DEFAULT '' COMMENT '题目来源',
  `prob_skills` VARCHAR (100) NOT NULL DEFAULT '' COMMENT '涉及知识点(多个之间用;分隔)',
  `create_by` VARCHAR (20) NOT NULL COMMENT '创建者用户名',
  `create_time` DATETIME NOT NULL COMMENT '创建时间',
  `update_by` VARCHAR (20) NOT NULL COMMENT '修改者用户名',
`update_time` DATETIME NOT NULL COMMENT '修改时间') ENGINE = INNODB COMMENT = '题目表';

CREATE TABLE `user_prob` (
  `user_id` INT NOT NULL COMMENT '用户ID',
  `prob_id` INT NOT NULL COMMENT '题目ID',
  `commit_count` INT NOT NULL DEFAULT 0 COMMENT '尝试次数',
  `check_count` INT NOT NULL DEFAULT 0 COMMENT '点击次数',
`ac_flag` CHAR(1) NOT NULL DEFAULT '0' COMMENT '是否通过(0表示未通过,1表示通过)') ENGINE = INNODB COMMENT = '用户题目表';

CREATE TABLE `login_log` (
  `log_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '日志ID',
  `log_des` VARCHAR (100) NOT NULL COMMENT '日志描述',
  `login_user` VARCHAR (20) NOT NULL COMMENT '登录用户名',
  `login_time` DATETIME NOT NULL COMMENT '登录时间',
  `login_location` VARCHAR (100) NOT NULL COMMENT '登录地点',
`login_sys` VARCHAR (100) NOT NULL COMMENT '使用的系统/浏览器') ENGINE = INNODB COMMENT = '登录日志';

CREATE TABLE `oper_log` (
  `log_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '日志ID',
  `oper_tag` VARCHAR (100) NOT NULL COMMENT '操作标识',
  `oper_user` VARCHAR (20) NOT NULL COMMENT '操作用户名',
  `oper_time` DATETIME NOT NULL COMMENT '操作时间',
  `oper_location` VARCHAR (100) NOT NULL COMMENT '操作地点',
`oper_sys` VARCHAR (100) NOT NULL COMMENT '使用的系统/浏览器') ENGINE = INNODB COMMENT = '操作日志';

CREATE TABLE `judge_record` (
  `record_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '记录ID',
  `prob_id` INT NOT NULL COMMENT '题目ID',
  `user_id` INT NOT NULL COMMENT '用户ID',
  `record_status` VARCHAR (20) NOT NULL COMMENT '测评状态',
  `judge_time` INT NOT NULL COMMENT '耗时(毫秒)',
  `record_code` LONGTEXT NOT NULL COMMENT '测评代码',
  `record_time` DATETIME NOT NULL COMMENT '测评时间',
`judge_lan` VARCHAR (20) NOT NULL COMMENT '语言') ENGINE = INNODB COMMENT = '测评记录';
CREATE TABLE `error_log` (`log_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '日志ID', `error_msg` LONGTEXT NOT NULL COMMENT '异常堆栈信息', `error_time` DATETIME NOT NULL COMMENT '发生时间') ENGINE = INNODB COMMENT = '异常日志';

CREATE TABLE `prob_supple` (
  `prob_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '题目ID',
  `multi_file` CHAR(1) NOT NULL DEFAULT '0' COMMENT '一个测试文件是否有多组测试数据(0表示没有)',
  `is_input` CHAR(1) NOT NULL DEFAULT '1' COMMENT '该题目是否有输入(1表示有)',
`difficulty` VARCHAR (50) NOT NULL DEFAULT '' COMMENT '题目难度') ENGINE = INNODB COMMENT = '题目的补充信息';

CREATE TABLE `rank` (`user_id` INT NOT NULL auto_increment PRIMARY KEY COMMENT '用户id', `ac_count` INT NOT NULL DEFAULT 0 COMMENT 'ac数量') ENGINE = innodb COMMENT = '排名';

CREATE INDEX idx_ac_count ON `rank` (`ac_count`);
