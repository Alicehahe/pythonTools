'''
 @author:HanLu
 @description:这段代码是用于巩固python的面向对象的知识点
 1、类和对象的定义
 2、实例话
 3、初始化方法self关键字、super方法
 4、方法的分类：普通方法、类方法、静态方法
 5、属性的防伪和设置：getter\setter方法--通过property属性方法或者装饰器来显示 @propetry @属性名.setter
 6、类的继承(子类对父类方法的重写，覆盖)
 7、类的多态
 8、属性的封装 __表示私有表示方法
 
'''


class Person:
    '''
    1、类的定义及类和对象的关系：
        1、通过class关键字来定义一个类
        2、类是对一类事物共同的特性做一个抽象的总结，对象是通过类模板实例话出来的，通过调用类名()
    2、类中的属性和方法
        方法：
            1、初始化方法==用于创建类的对象
            2、普通方法      需要通过类的实例话后，才能正常调用
            3、类方法        被@classmehtod修饰，方法的第一个参数为cls，可通过类名直接调用
            4、静态方法      被@staticmethod修饰，可直接通过类名调用
            5、self关键字    指的是self会指向当前创建对象的地址，代表的是当前创建的对象

        属性：
            1、设置setter、getter方法 ==通过装饰器@propetry @属性名.setter来设置
            2、属性设置为私有的，通过加__name,表示私有化
    3、类的特性
        1、类的继承
            1、通过(父类的名字)
            2、重写父类的方法
            2、子类中调用父类的方法 super()

        2、类的多态
            父类的引用指向子类的地址，就会发生多态
            python的多态比java中更加的灵活，只要类中存在名字相同的方法，传递不同的对象，就可以实现多态
            就说明不一定是子类的关系，都可以发生多态

    '''

    def __init__(self,name,age):
        self.__name = name  #_属性私有权限设置方法一：name这里书面上表示为：私有属性
        self.age = age

    #间接访问属性通过配置set、get方法 装饰器@property表示get方法 @属性名.setter表示set方法
    @property
    def ageinfo(self):
        print('getter')
        return self.age

    @ageinfo.setter
    def ageinfo(self,age):
        self.age = age
        print('setter')

    #这是一个普通方法
    def test_person_info(self):
        print('这是Person类的test_person_info方法')

    #定义一个类方法
    @classmethod
    def test_class_method(cls):
        print("this is class method")

    #定义一个静态方法
    @staticmethod
    def test_static_method(self):
        print("this is static method")



class teacher(Person): #类的继承在子类的括号中写上父类的类名

    def __init__(self,name,age,subject):
        super().__init__(name,age)  #子类中调用父类的初始化方法
        self.subject = subject

    #重写了父类中定义的方法，实现自己想要的功能
    def test_person_info(self):
        print("这是老师类中重写的方法")

    def test_teacher_info(self):
        print(self.name,"的年龄为：",self.age,"教的科目是：",self.subject)


#定义一个新的方法，用于实现类的多态
def test_class_polymorphism(object):
    print(object.test_person_info())




person_001 = Person('Dale',40)
#person_001.test_person_info()
# person_001.ageinfo = 100
# print(person_001.ageinfo)
# Person.test_class_method()
# Person.test_static_method()
# Person.test_person_info(Person)
# teacher.test_person_info(teacher)
#person_001.name = 'hanlu'       #会报错  AttributeError: 'Person' object has no attribute 'name'

teacher_001 = teacher('teacher001',28,"英语")
# teacher_001.test_teacher_info()
# teacher_001.test_person_info()


#实现多态
test_class_polymorphism(person_001)
test_class_polymorphism(teacher_001)