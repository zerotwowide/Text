# # 列表生成式
# my_list = [x * x for x in range(1,11) if x % 2 == 0]
# print(my_list)
#
# # 双层循环 生成全排列
# double_list = [m+n for m in 'ABC' for n in 'XYZ']
# print(double_list)

# # 迭代（遍历）
# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# for k, v in d.items():
#     print(k, '=', v)

# # 生成器：generator
# g = (x * x for x in range(10))
# for n in g:
#     print(n,end=',')
# print(type(g))

