from pymysql import Connection

# 构建MySQL到数据库的连接
conn = Connection(
    host='localhost',   # 主机名
    port=3306,          # 端口
    user='root',        # 账户
    passwd='Liu0716',   # 密码
    database='test',    # 选择数据库
    autocommit=True,     #设置自动提交
    charset='utf8'
)   # 传参要指定传参

# 获取游标对象
cursor = conn.cursor() # 用来执行相关操作

# 使用游标对象，执行 sql 语句
# cursor.execute("select * from student;")  # 查询表中数据
# results = cursor.fetchall()   # 获取结果
# for r in results:   # 打印结果
#     print(r)

# 插入数据
cursor.execute("insert into teacher values(4, '三玖', 17)")
# conn.commit()   # 提交命令

conn.close()
