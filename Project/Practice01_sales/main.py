from fileReader import TextFileReader,JsonFileReader
from data_define import Record
from pymysql import Connection
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

txt_file_reader = TextFileReader("D:\\2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:\\2011年2月销售数据JSON.txt")

# 记录一月和二月的数据 list[Record]
jan_data:list[Record] = txt_file_reader.data_record()
fab_data:list[Record] = json_file_reader.data_record()

# 创建一个 all_data list[Record] 接收所有的数据
all_data:list[Record] = jan_data + fab_data

conn = Connection(
    host='localhost',   # 主机名
    port=3306,          # 端口
    user='root',        # 账户
    passwd='Liu0716',   # 密码
    database='practice01',  # 选择数据库
    autocommit=True,        # 设置自动提交
    charset='utf8'
)

cursor = conn.cursor()

for record in all_data:
    sql = f"insert into sales_data(sales_date,sales_id,money,province)"\
          f"values ('{record.date}','{record.order_id}','{record.money}','{record.province}')"
    cursor.execute(sql)
conn.close()
# # 利用字典储存统计后的数据
# data_dict:dict = {}
# for my_data in all_data:
#     if my_data.date in data_dict.keys():
#         data_dict[my_data.date] += my_data.money
#     else:
#         data_dict[my_data.date] = my_data.money
# print(data_dict)
#
# # 数据可视化
# bar = Bar(init_opts=InitOpts(theme=ThemeType.DARK))
#
# bar.add_xaxis(list(data_dict.keys())) # 接收list 类型
# bar.add_yaxis("销售额", list(data_dict.values()),label_opts=LabelOpts(is_show=False))
# bar.set_global_opts(
#     title_opts=TitleOpts(title="每日销售额")
# )
# bar.render("每日销售额柱状图.html")