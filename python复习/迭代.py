# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    # 先判断是否为非空list
    if (L == []):
        return (None, None)
        # 查找最大值和最小值
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if i > max :
                max = i
            if i < min :
                min = i
        print(f'max={max}, min={min}')
        return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('1测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('2测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('3测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('4测试失败!')
else:
    print('测试成功!')