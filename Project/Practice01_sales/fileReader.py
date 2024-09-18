import json

from data_define import Record
# 定义抽象类确定要实现的功能
class FileReader:
    # 将文件数据转换为 record 对象，并将数据封装在 list 中
    def data_record(self)-> list[Record]:
        pass


# 定义子类 Txt 类型文件实现父类功能
class TextFileReader(FileReader):
    # 接收数据文件地址
    def __init__(self,path):
        self.path = path

    # 复写父类方法,实现功能
    def data_record(self):
        record_list: list[Record] = []
        f = open(self.path,"r",encoding="utf-8")
        for line in f.readlines():   # 按行输出
            line = line.strip()    # 消除字符串首尾空格和换行符号
            data_list = line.split(",") # 将字符串按照 "," 分隔开形成一个新的列表
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)
        f.close()
        return record_list

# 定义子类 JSON 类型文件实现父类功能
class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path = path

    # 复写父类方法,实现功能
    def data_record(self):
        record_list: list[Record] = []
        f = open(self.path,"r",encoding="utf-8")
        for line in f.readlines():
            data_dict = json.loads(line)    # 将 JSON 转换为 dict 类型
            record = Record(data_dict["date"],data_dict["order_id"],data_dict["money"],data_dict["province"])
            record_list.append(record)
        f.close()
        return record_list

if __name__ == '__main__':
    f1 = TextFileReader("D:/2011年1月销售数据.txt")
    f2 = JsonFileReader("D:/2011年2月销售数据JSON.txt")
    f1.data_record()
    f2.data_record()
    for i in f1.data_record():
        print(i.__str__())
    print("---------------------------------------------------------------")
    for i in f2.data_record():
        print(i.__str__())