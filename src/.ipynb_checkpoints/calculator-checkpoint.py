def fun1(x, y):
    return x+y
def fun2(x, y):
    return y-x
def fun3(x, y):
    return x*y
def fun4(x, y):
    final_sum = 0
    final_sum +=fun1(x,y)
    final_sum +=fun2(x,y)
    final_sum +=fun3(x,y)
    return final_sum
 
if __name__=='__main__':
    print(fun4(2,3))