import os

# os.walk()遍历文件夹下的所有文件
# os.walk()获得三组数据(rootdir, dirname,filnames)
def file_path(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)    # 当前目录路径
        print(dirs)    # 当前路径下的所有子目录
        print(files)            # 当前目录下的所有非目录子文件
        for file in files:      # 显示子文件的完整路径
            # print(os.path.realpath(file))        # 这个地方有问题！！！显示的不是真实路径
            print(root + "\\" + file)                     # 这个才是对的
file_path(r"D:\pythontest\selenium")
# file_path(os.getcwd())
# print(os.listdir(r"D:\pythontest\selenium"))    
# print(os.listdir())     # 只显示该目录下的文件名和目录名，不包含子目录中的文件，默认为当前文件所在目录
# print(list(os.walk(r"D:\pythontest\selenium")))   # 用os.walk生成列表 


