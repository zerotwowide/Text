# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法

def trim(s):
    # while s and s[0] == ' ':
    #     s = s[1:]
    # while s and s[-1] == ' ':
    #     s = s[:-1]
    # return s

    start = 0
    while start < len(s):
        if s[start] == ' ':
            start += 1
        else:
            break
    bottle = len(s)-1
    while bottle >= 0:
        if s[bottle] == ' ':
            bottle -= 1
        else:
            break
    return s[start:bottle+1]

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')