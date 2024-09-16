from itertools import count

from Project.Practice02_book.Book_func import BookFunc,AchFunc
from Project.Practice02_book.Book import Book
text = AchFunc()
dep_book: list[Book] = []

# 操作页面
print("------图书管理系统------")
judge = input("请输入你要进行的操作：\n"
              "1 录入书籍\n"
              "2 查找书籍\n"
              "3 删除书籍\n")
print("------------------------")
if judge == "1":
    num:int =int(input("请输入你要录入的书籍数量："))
    for i in range(1, num+1):
        print(f"录入的第{i}本书")
        dep_book = text.deposit_book()
        # 录入后的图书信息
        print("录入完成的图书信息为")
        for book in dep_book:
            print(book.__str__())
elif judge == "2":
    find_book = text.find_book()
    print(f"查找的书籍信息为：{find_book}")
elif judge == "3":
    text.delete_book()
    print("删除后的图书信息为：")
    for book in dep_book:
        print(book.__str__())
else:
    print("输入错误，关闭系统")