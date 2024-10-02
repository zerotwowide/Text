# 输入一个四位整数，反向输出对应四位数
# 1234 --> 4321
num = input("请输出一个四位数数字：")
def reverse(num):
    num = num[::-1]
    num = int(num)
    return num

if __name__ == '__main__':
    result = reverse(num)
    print(result)