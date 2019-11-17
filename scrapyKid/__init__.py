import pymysql

# Django 在连接 MySQL 数据库时默认使用的是 MySQLdb 驱动，没有安装该驱动，因为它并不支持 Python3，
# 安装的是 PyMySQL 驱动，让当前的 Django 通过 PyMySQL 来连接 MySQL 数据库
pymysql.install_as_MySQLdb()

