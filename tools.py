
def is_sushu(num):
    """验证数字是否为素数"""
    res = True
    if not isinstance(num, int):
        print('输入的不是整数：%s'%str(num))
        return False
    for x in range(2, num-1):
        if num%x==0:
            res=False
            return res
    return res
