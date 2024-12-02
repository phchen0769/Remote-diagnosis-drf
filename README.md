# remote_diagnosis_drf
# logs 目录为日志文件以及uwsgi和nginx运行时产生的临时文件。
# supervisor.conf 为supervisord工作时的配置文件
# uwsgi.ini 为uwsgi的配置文件
# repositories 为alpine国内源文件
# requirements.txt为项目需要安装的依赖包

############### 1 #################
# 运行Mariadb数据库
# docker run -d --name Mariadb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -v /Volumes/myDriver/github/db/mariadb:/var/lib/mysql mariadb:latest

# 运行postgre数据库
# docker run -d --name Postgres -p 5432:5432 -e POSTGRES_PASSWORD=123456 -v /Volumes/myDriver/github/db/postgresql:/var/lib/postgresql/data postgres:latest

############### 2 #################
# 创建数据库 Mariadb
# 数据库名：remote_diagnosis
# 字符集： utf8mb4
# 排序规则：utf8mb4_general_ci

# 创建数据库 Postgre
# 数据库名：remote_diagnosis
# 所有者：postgres
# 模版：postgres
# 表空间： pg_default

############### 3 #################
# 注意：数据库创建表格，请使用全小写
# DB_tools中的工具使用，请在项目根目录中运行:
# 1.DB_tools/sys_import.py
# 2.DB_tools/data_import.py

############### 5 #################
# 运行项目 F5 或
# python manage.py runserver

