'''
 @author:HanLu
 @description:这是练习python对文件的读写操作、以及对文件/目录的操作
 知识点：
 1、文件存储的原理
    文件的是存储在磁盘上的，最终是以二进制进行存储
    文件可以分为两类：
        1、可以用文本打开，正常查看文件内容的
        2、二进制文件，通过文本打开是乱码的文件，例如：视频、图片等等

 2、文件的常规操作：打开、读写、关闭
 3、文件打开模式
 4、文件读、文件写 都是文件和内存之间的交流，从文件读入内存，数据从内存写入文件
 4.1、实现一个文件的粘贴复制
 5、对文件、目录的操作
 
'''
import  os

class OperaFile():

    #1、定义一个读文件操作方法 使用read/readline方法读文件（文件必须存在，和windows操作一致，不存在文件无法去打开）
    def readfile(self,filepath):
        # with open(filepath) as f:  #默认是只读模式，将文件内容读入内存
        #     print('使用read方法去读:',f.read(),end='\n')

        file = open(filepath,'r')
        while True:
            content = file.readline()
            print(content,end='')
            if not content:  #这里的判断，需要拿上一次读到的内容去判断，不可以用file.readline直接去判断，因为相当于又读了一次，所以会出现间隔读取
                break
        file.close()

    #2、定义一个写文件方法 使用write方法，将内存数据写入新文件中
    def writefile(self,filepath2):

        #通过w和x两种模式打开文件
        # w模式，当文件不存在时，会自动创建文件
        # w模式，重复调用时，会将原来的文件内容删除后，添加新的文件内容
        # with open(filepath2,'w') as f:
        #     f.write('这是需要写入的文件内容,这是新的文件内容')

        # a模式，当文件不存在时，也会自动创建文件
        # a模式，重复调用时，会在原来文件末尾处，追加文件内容
        with open(filepath2,'a') as f2:
            f2.write('这是通过a模式打开文件，会在文件末尾处追加文件内容')



    #3、定义一个文件方法，对二进制文件进行复制粘贴操作,二进制文件读取一般只用read方法
    def read_write_binaryfile(self,srcpath,dstpath):

        #创建一个文件对象-用于只读,文件以只读的方式打开，二进制方式进行读
        with open(srcpath,'rb') as f1:
            with open(dstpath, 'wb') as f2:
                print('正在读文件......')
                content = f1.read() #一次性读入
                print('正在写文件.......')
                f2.write(content)


    #4、定义一个方法，使用os模块，对文件进行操作
    def os_opera_file(self):
        try:
            #对文件进行操作:重命名、删除一个文件
            os.rename('/Users/qingjiao/Desktop/old.jpeg','/Users/qingjiao/Desktop/newname.jpeg')
            #os.remove('/Users/qingjiao/Desktop/newname.jpeg')
        except FileNotFoundError:
            print(FileNotFoundError.filename)
        finally:
            print("再见")

#OperaFile().readfile('/Users/qingjiao/Desktop/test_readfile.txt')
# OperaFile().writefile('/Users/qingjiao/Desktop/test_writefile2.txt')
#OperaFile().read_write_binaryfile('/Users/qingjiao/Desktop/old.jpeg','/Users/qingjiao/Desktop/new.jpeg')
OperaFile().os_opera_file()