import pymysql #pip install pymysql

conn = pymysql.connect(host="localhost",user="root",password="",db="ta")

q = conn.cursor()