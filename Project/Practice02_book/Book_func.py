from  Project.Practice02_book.Book import Book

# 设计抽象类，确定要实现的功能
class BookFunc:
    # 存入图书
    def deposit_book(self):
        pass
    # 查找图书
    def find_book(self):
        pass
    # 删除图书
    def delete_book(self):
        pass

# 设计子类，实现功能
book_list: list[Book] = []
class AchFunc(BookFunc):
    def deposit_book(self):
        bookName = input("Enter deposit book name: ")
        boolISBN = input("Enter deposit ISBN number: ")
        book = Book(boolISBN, bookName)
        book_list.append(book)
        return book_list

    def find_book(self):
        bookFindName = input("Enter find book name: ")
        for book in book_list:
            if book.name == bookFindName:
                return book

    def delete_book(self):
        bookName = input("Enter want delete book name: ")
        for index in book_list:
            if index.name == bookName:
                book_list.pop(book_list.index(index))

# 测试
if __name__ == "__main__":
    func = AchFunc()
    p =None
    for i in range(1,4):
        print(f"录入的第{i}本书")
        p = func.deposit_book()
    for book in p:
        print(book.__str__())

    q = func.find_book()
    print(f"你寻找的书籍信息为：{q}")
    func.delete_book()
    for book in p:
        print(book.__str__())