# num: int = eval(input("请输入要打印的正三角形行数："))
# for row in range(1,num+1):
#     # 打印空格
#     for i in range(1,num+1-row):
#         print(" ",end='')
#     # 打印 *
#     for j in range(1,2*row):
#         print("*",end='')
#     print()


# 打印倒三角形
# num: int = eval(input("请输入要打印的倒三角形行数："))
# for row in range(1,num+1):
#     print(" " * row ,end="")
#     print("*" * (2*num-1+(row-1)*(-2)),end="")
#     print()



'''
$$$*
$$***
$*****
*******
$*****
$$***
$$$*
'''
# # 打印菱形
# num = eval(input("请输入要打印的菱形行数："))
# top = int((num+1)/2)
# for i in range(1,top+1):
#     print(" " * (top-i),end='')
#     print("*" * (1+(i-1)*2),end='')
#     print()
# bottom = num-top
# for j in range(1,bottom+1):
#     print(" " * j,end='')
#     print("*" * (2*bottom-1+(j-1)*(-2)),end='')
#     print()