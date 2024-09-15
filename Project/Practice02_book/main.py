from Project.Practice02_book.Book_func import BookFunc,AchFunc

text = AchFunc()
dep_book = None
for i in range(1,3):
    print(f"录入的第{i}本书")
    dep_book = text.deposit_book()
# 录入后的图书信息
for book in dep_book:
    print(book.__str__())

find_book = text.find_book()
print(f"你查找的书籍信息为：{find_book}")
text.delete_book()
# 打印处理后的图书信息
for book in dep_book:
    print(book.__str__())