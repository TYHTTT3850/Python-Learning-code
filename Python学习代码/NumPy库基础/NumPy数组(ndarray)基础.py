"""
numpy库两个基本的类: 1、ndarray(n-dimensional-array)，存储单一数据类型的多维数组。
                    2、ufunc(universal function)，能够对数组进行处理的通用函数。
"""
import numpy as np

"""--------------------数组创建--------------------"""
print("--------------------数组创建--------------------")
# array()方法。
a = np.array([1,2,3,4,5,6]) #一维数组
b = np.array([[1,2,3],[4,5,6]],dtype=np.float64) #二维数组，并指定数据类型为双精度浮点
print(a,b,sep='\n')

# 其他创建数组方法。
a = np.arange(4) #np.arange(起点,末尾,间距) 不包括末尾
b = np.arange(0,10,2)
c = np.empty([2,3]) #创建2×3的整型空矩阵
d = np.eye(3) #创建三阶单位阵
e = np.zeros([3,3]) #创建三阶全0矩阵
f = np.ones([3,3]) #创建三阶全1矩阵
g = np.linspace(0,10,11,dtype=int) #在起点和末尾之间生成指定数量的数
print(a,b,c,d,e,f,g,sep='\n',end='\n\n')

"""--------------------数组属性--------------------"""
print("--------------------数组属性--------------------")
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
# ndim，ndarray类属性。返回数组的维数。
print("维数：",a.ndim)

# shape，ndarray类属性。数组的尺寸，封装在元组内，二维m×n的数组为(m,n)，高维也类似。
print("尺寸：",a.shape)

# size，ndarray类属性。数组的元素总数
print("元素总数：",a.size)

# dtype，ndarray类属性。数组的数据类型
print("数据类型",a.dtype)

# itemsize，ndarray类属性。数组每个元素占用的空间大小
print("每个元素占用的空间大小：",a.itemsize,end="\n\n")

"""--------------------数组索引--------------------"""
print("--------------------数组索引--------------------")
a = np.array([1,2,3,4,5,6,7,8,9])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# 一般索引。数组名[i,j]
print(a[1]) #一维数组索引，一次索引单个
print(a[[2,3,5]]) #一维数组索引，一次索引多个
print(b[1,2]) #二维数组索引，输出第二行第三列元素
print(b[1]) #二维数组索引，输出第二行所有元素
print(b[1,:]) #二维数组索引，输出第二行所有元素
print(b[:,1]) #二维数组索引，输出第二列所有元素
print(b[1:3,0:2]) #二维数组索引，输出第二、三行，第一、二列所有元素
print(b[[0,2],0:2]) #二维数组索引，输出第一、三行，第一、二列所有元素
print(b[[0,2],[0,2]]) #二维数组索引，输出第一行第一列、第三行第三列元素

# 布尔索引
print(b[b>4],end="\n\n")

"""--------------------数组修改--------------------"""
print("--------------------数组修改--------------------")
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
#修改单个元素
x[2,0] = -1
print(x)

# delete()方法
y = np.delete(x,2,axis=0) #删除第三行
z = np.delete(x,2,axis=1) #删除第三列
print(y,z,sep='\n')

# append()方法
t1 = np.append(x,[[10,11,12]],axis=0) #沿垂直方向增加一行
t2 = np.append(x,[[10],[11],[12]],axis=1) #沿水平方向增加一列
print(t1,t2,sep='\n',end="\n\n")

"""--------------------数组变形--------------------"""
print("--------------------数组变形--------------------")
a = np.arange(1,11) #生成1-10的一维数组
print(a)

# reshape()方法，ndarray类方法。返回变形后的新数组，不改变原数组。
b = a.reshape(2,-1) #填入-1表示自动计算变形成两行后有几列
print(a,b,sep='\n')

# resize()方法，ndarray类方法。没有返回值，直接改变数组本身。
a.resize(2,5)
print(a)

# transpose()方法，ndarray类方法。数组转置，返回转置后的新数组，不改变原数组。
b = a.transpose()
c = a.T #等同于a.transpose()
print(a,b,c,sep='\n')

# flatten()方法，ndarray类方法。返回水平展开后的新数组，不改变原数组。
d = a.flatten()
print(a,d,sep='\n',end='\n\n')

"""--------------------数组组合--------------------"""
print("--------------------数组组合--------------------")
a = np.array([[0,1,2],[3,4,5],[6,7,8]])
b = np.array([[9,10,11],[12,13,14],[15,16,17]])

# hstack()方法。沿水平方向组合数组,传入参数为元组，返回数组。
h = np.hstack((a,b))
print(h)

# vstack()方法。沿垂直方向组合数组,传入参数为元组，返回数组。
v = np.vstack((a,b))
print(v)

# dstack()方法。沿深度方向组合数组,传入参数为元组,返回数组。
d = np.dstack((a,b))
print(d,end="\n\n")

"""--------------------数组分割--------------------"""
print("--------------------数组分割--------------------")
a = np.array([[1,2,3],[4,5,6],[7,8,9]])

# hsplit()方法。沿水平方向分割，返回数组列表。
h:list[np.ndarray] = np.hsplit(a,3) #等分为三个3×1数组
print(h)

# vsplit()方法。沿垂直方向分割，返回数组列表。
v:list[np.ndarray] = np.vsplit(a,3) #等分为三个1×3数组
print(v)

# dsplit()方法。沿深度方向分割，返回数组列表。
b = np.array([[[0,1,2],[3,4,5],[6,7,8]],[[9,10,11],[12,13,14],[15,16,17]]])
d:list[np.ndarray] = np.dsplit(b,3) #等分为三个2×3×1数组
print(d,end="\n\n")

"""--------------------数组运算--------------------"""
print("--------------------数组运算--------------------")
a = np.array([[1,1,1],[1,1,1],[1,1,1]])
b = np.array([[2,2,2],[2,2,2],[2,2,2]])

# 对应位置元素加，减，乘，除。
c = a+b;d=a-b;e=a*b;f=a/b
print(c,d,e,f,sep='\n')

# 对应位置取余，整除，幂次。
g = a%b;h=a//b;i=a**b
print(g,h,i,sep='\n')

# 矩阵乘法
j = a@b
k = np.dot(a,b) #等同于@运算符
print(j,k,sep='\n')

# 对应位置比较运算，得到布尔值数组。
a = np.array([[3,4,9],[12,15,1]])
b = np.array([[2,6,3],[7,8,12]])
c = a>b ; d = a>=b ; e = a<b ; f = a<=b ; g = a!=b ; h= a==b
print(c,d,e,f,g,h,sep='\n')
