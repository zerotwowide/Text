import json
from pymysql import Connection

# 连接数据库
conn = Connection(
    host='localhost',
    user='root',
    passwd='Liu0716',
    db='practice01',
    charset='utf8',
    autocommit = True
)

cursor = conn.cursor()  # 获取游标对象
cursor.execute("select * from sales_data")
result: tuple = cursor.fetchall()   # result 记录查寻的数据

# 使用文件接收创建的数据
f = open("D:/mysql_text.txt","a",encoding="utf-8")  # 创建打开文件
data_dict = {}
# 利用循环将数据写入文件
for record in result:
    data_dict["data"] = str(record[0])
    data_dict["order_id"] = record[1]
    data_dict["money"] = int(record[2])
    data_dict["province"] = record[3]
    f.write(json.dumps(data_dict, ensure_ascii=False))
    f.write("\n")

f.close()   # 关闭文件
conn.close()