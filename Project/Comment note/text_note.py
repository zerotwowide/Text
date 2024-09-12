# 变量类型注解
from typing import Union

name: str = "蔡徐坤"        # 第一种方法
demo = "csgo2" # type:str  # 第二种方法

# 函数和方法注解
def add(x:int,y:int):      #形参类型注解
    return x+y
add(1,2) # ctrl + p

def sub(x:int,y:int)->int: # ->返回值类型注解
    return x-y
re_sub = sub(2,1)

# Union类型注解   使用前要导包
my_list: list[Union[int,str]] = [1,2,3,"qian","lisi"]
my_dict: dict[str,Union[str,int]] = {"name":"芊芊","age":17}
# 同理，也可以用在函数和方法里面