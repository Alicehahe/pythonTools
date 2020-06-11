'''
 @author:HanLu
 @description:这个脚本是巩固python的基础知识点，知识点如下：

 1、注释的三种表现形式
 2、基础的数据类型
 3、运算符
 4、变量
 5、列表、元祖数据类型的定义和使用
 6、字典、集合数据类型的定义和使用
 7、判断语句
 8、循环语句
 9、break/continue
 10、函数的定义及使用
'''


def testcomment():
    '''
    这个函数是用于练习python的注释
    :return:
    '''

    print("这一行被注释后，不会被执行") #这是单行注释

    '''
    print("这是换行多文本注释")
    print("这是换行多文本注释")
    print("这是换行多文本注释")
    print("这是换行多文本注释")'''


    '这是长文本注释'

def testvartype():
    '''
    这个函数是用于练习python的基本数据类型
    :return:
    '''

    #1、python的基础数据类型有以下几种：整形、浮点型、字符串、布尔类型、空值(None)
    a = 1           #整形 python3无int、long区别，最长可放long类型的数值
    b = 1.23        #浮点型 无长度限制，超过长度会显示inf
    c = 'hello'     #字符串类型 可用单引号表示，python中无字符类型
    d = "hello"     #字符类型 也可用双引号表示
    e = True        #布尔类型 True表示结果为真
    f = False       #布尔类型 False表示结果为假
    g = None        #空值 python中一切解皆对象，当指向的对象地址为空的时候，表示为None

def testvarcal():
    '''
    练习python的运算符、变量
    :return:
    '''

    #1、算术运算符
    a = 1+2
    b = 4-3
    c = 4*3
    d = 6//3        #知识点：整除，结果一定是int类型
    d_float = 6/3   #知识点：非整除，结果一定是float
    e = 8%3
    f = 2**3

    #2、关系运算符
    1 >= 2
    2 == 3
    4 <= 5

    #3、赋值运算符
    g = 1+1

    #4、逻辑运算符
    print((1>2) and (3==4))

    print((5==5) or (1<4))

    print(not (3==3))


    #5、成员运算符
    print('a' in 'abcd')

    print(a,b,c,d,d_float,e,f,g)
    print(type(d))


    #6、常量、变量的定义和命名规范
    '''
    1、定义
        用于存储各种数据类型存储的地址，变量可重复访问数据，变量是指向数据的内存地址位置
        
    2、命名规则
        变量是由：字母、数字、下划线组成
        开头只能是字母、下划线，数字不可开头
        不可和python的内置关键字相同，如果定义相同会将关键字原有的功能覆盖
        变量一般都是小写
        常量一般是全部大写，只是规定，可以修改无关键字修饰约束
    '''
    age = 18
    name = "hanlu"

    #0age = 19 #错误 会抛异常：invalid syntax

    #if = 12 #错误 会抛出异常 ：invalid syntax

    PI = 3.1415926 #常量

def test_list_tuple():

    '''
    这是练习python的扩展数据类型：列表、元祖的定义和常见操作
    :return:
    '''

    '''
    1、列表定义
        是一组有序可变的数据集合(有序、存储不同数据类型、可变)
        
    2、列表的使用
        列表是一组可变的数据集合，可以使用列表包中一些函数对列表进行操作
            增加列表元素 append/insert
            删除列表元素 remove/pop   del关键字
            修改列表元素 list[0] = 1 通过下标的方式进行赋值
            输出列表元素 通过下标循环打印列表元素,可以通过正序下标1/2/3 也可以通过倒序下标-1/-2/-3
    '''
    #1、定义一个列表的两种形式，存储不同的数据类型
    lis = [18,'hanlu',['father','mother','son'],True,160.45] #列表中可以存储任意的数据类型
    print('lis第一版内容为：',lis)

    #1.1、通过list()方法，传入一个任意类型的序列(字符串、元祖、key-value)都可以自动转换成list
    lis_001 = list((1,'hanlu','great'))
    print(lis_001)

    #2、对列表元素进行增、删、改、查
    lis.append('new_001_ele')
    lis.insert(0,'new_002_ele')

    print('增加元素后lis内容为：',lis)

    lis.remove('new_002_ele')
    lis.pop(-1)

    print('删除元素后lis内容为：',lis)

    lis[0] = 25
    print('修改元素后lis内容为：',lis)


    for i in lis:
        print(i,end='\t')  #将print默认结尾的换行改为\t制表符




    '''
    1、元祖定义
        是一组有序不可变的数据集合(有序、存储不同数据类型、不可变)
        
    2、元祖的使用
        元祖是一组不可变的数据集合，所以只能进行数据的打印
            输出元祖元素 通过下标循环打印
    
    '''
    #1、定义一个元祖，存储不同的数据类型
    tup_001 = (18,) #定义一个只有一个元素的元祖，需要加上逗号， 和(18)区分开
    tup = (18,'hanlu',['father','mother','son'],True,160.45)
    print()
    #2、对元祖的操作，输出元祖内容
    for i in tup:
        print(i,end='\t')

def test_dict_set():
    '''
    练习python的字典、集合的定义和常见操作
    :return:
    '''

    '''
    1、字典的定义
        字典是用一组无序可变的key-value集合，通过访问key值，可以访问对应的value
        
    2、字典的常见规则和操作
        规则：
            1、字典的key值一定要是不可变数据类型(不可变表示：对数据做修改后不会改变原来变量的值，而是生成一个新的对象)，整数、字符串
            2、key值不可以重复，如果对一个key重复赋值，后面的值会覆盖前面key所存储的值
            3、每次输出字典的内容，输出的顺序都是不以牙膏的，因为字典是无序的
        操作：
            1、输出字典的key所对应的value值
            2、修改字典key所对应的value值
            3、增加一组新的key-value值
            4、循环遍历字典的3种方法：
                遍历key-value，分别打印到不同的变量中，使用.items()函数
                遍历输出所有的keys,只输出字典中所有的key值，无序的(顺序可以通过sort()/sorted()来改变)
                遍历输出所有的values，只输出字典中所有的value值，无序(顺序可以通过sort()/sorted()来改变        
    
    '''
    #1、定义一个字典
    dic_001 = {'name':'hanlu','age':18,'class':'初三'} #简单的字典

    #定义一个复杂的字典，即字典的key值对应另一个字典
    dic_002 = {
        'Mary':{'name':'Mary','age':35},
        'Geroge':{'name':'Geroge','age':38},
        'Missy':{'name':'Missy','age':12},
        'Shiery':{'name':'Shiery','age':10}
    }

    #2、字典的操作
    #2.1、通过key值访问对应的vaule、修改对应的value，增加对应的key-value对
    print(dic_001['name'])
    print(dic_001['age'])
    print(dic_001['class'])
    print('dict_001字典内容为：',dic_001)

    #通过key值修改value值
    dic_001['age'] = 20

    #增加字典内容
    dic_001['sex'] = 'man'
    dic_001['hobbies'] = 'execrise'

    print('dict_001字典内容为：',dic_001)


    #2.2、遍历字典
    #通过items方法，遍历key-value值
    for name,info in dic_002.items():
        print(name,'的个人信息为：',info)

    #通过遍历所有的key值
    for name in dic_002.keys():
        print('用户的姓名为：',name,end='\t')

    print()

    #通过遍历所有的vaule值
    for info in dic_002.values():
        print(info,end='\t')
    print()


    '''
    1、集合的定义
        是一组不可重读的keys集合
        
    2、集合的规则和常见操作
        规则：
            1、集合内部不可出现重复的数值，set也会自动过滤
            2、定义一个集合需要传入一个列表
        常见操作：
            1、集合取交集，只输出都有的元素
            2、集合取并集，将所有的不重复元素合并输出
    
    '''
    #1、定义一个集合
    set_001 = set([1,2,3])  #传入一个列表
    set_002 = set([2,3,4,5])


    #2、对集合进行交集、并集的操作,输出也是一个集合
    print(set_001 & set_002)
    print(set_001 | set_002)

def testmethod(x,y):
    '''
    1、函数的定义和调用
        def method():
            print('test')

        method()

        1、通过def来定义一个函数
        2、mehtod为方法名，()中输入形式参数，:表示函数方法体开始
        3、print()表示方法体内容
        4、method()表示方法的调用

    2、函数的形参、实参、参数默认值、return返回值
        形参和实参数的定义：
            1、方法定义时，传入的参数为形式参数
            2、方法调用时，传入的参数为实际参数
        参数传递的几个方式：
            1、位置传递
            2、关键词传递
            3、关键词+位置传递
            4、可变参数 ---将传入的可变长度的参数默认组装成元祖 *args
            5、关键词参数 ---将关键词参数在函数内部自动组装成一个dict **kw

        规则：
            函数的参数一定要是不可变数据类型
    :return: int sum
    '''
    sum = x + y
    return sum


def method_canshu(age,name=None): #位置参数一定要摆在关键词参数前面
    print('age is:',age,'name is:',name)


def method_unsuretuple(name,*score):
    print(name,'的语文、英语的成绩为：',score)
    for i in score:
        print(i)
        print(type(score))



def method_unsure_kw(name,**kw):
    print(name,'的个人信息为：',kw)

    for key,value in kw.items():
        print(key)


if __name__ == '__main__':
    test_list_tuple()
    #test_list_tuple()
    #testvarcal()
    #test_dict_set()
    #sum = testmethod(2,3)
    #print(sum)
    #method_canshu(20)
   # method_canshu(age=18,name='hanlu') #关键词参数
   # method_unsuretuple('hpp',80,99) #这是传入了两个元祖
   # method_unsuretuple('dcp',(90,99)) #这是传入了一个整体元祖
   # method_unsure_kw('hanlu',age=18,math_score=99,sex='woman')  #以关键字的形式传入key-value值