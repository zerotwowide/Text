class Animal:   # 抽象类：定义了一些抽象方法，要求子类必须实现
    def speak(self):   # 抽象方法
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

dog = Dog()
cat = Cat()
# 多态：同样的行为，使用不同对象，实现不同目的
def text(animal: Animal):
    animal.speak()

if __name__ == '__main__':
    text(dog)
    text(cat)