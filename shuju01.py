'''
题目001：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
def tm001():
    '''
    【个人备注】：按题意直接写出来
    '''
    arr = []
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                num = 100*i+10*j+k
                if i!=j and j!=k and i!=k and num not in arr:# 互不相同且无重复数字的三位数
                    arr.append(num)
    print(len(arr),arr)
x = tm001()
print(x)

''' 
def tm001_1():
   
    【个人备注】：其实python自带排列组合模块，可以直接调用。
    也知道这个写法，只是函数记不住，还是百度一下才能写出来。
    如果这是面试题，能写出后一种当然好，不能的话还是老老实实的按照上面的思路来吧。
    
    import itertools
    temp_arr = list(itertools.permutations([1, 2, 3, 4], 3)) # 排列  # A_4^3 = (4)!/(4-3)! = (4*3*2*1)/1 = 24
    arr = [100*t[0]+10*t[1]+t[2] for t in temp_arr]
    print(len(arr),arr)
'''
'''
 ———————————————— 
版权声明：本文为CSDN博主「songlh1234」的原创文章，遵循CC 4.0 by-sa版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/songlh1234/article/details/91391981

'''
