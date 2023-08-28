
import os
import sys
import shutil


"""
打印日志

:param string msg
    日志内容
:param string logfile
    日志文件名
"""
def log(msg,logfile='crypt_util.log'):
    with open(logfile,'a') as f:
        f.write(msg)


"""
打印日志并输出

:param string msg
    打印内容
"""
def print_log(msg):
    log(msg)
    print(msg)


"""
生成加密代码

:param f string
    原始文件,加密后将替换内容

"""
def make(filename):
    with open(filename,mode='r',encoding='utf-8-sig') as f:
        dat = ''.join([ bin(c)[2:].zfill(8) for c in f.read().encode()])
        with open(filename,mode='w',encoding='utf-8') as f:
            f.write("""
data='''%s''' 
exec(bytes([ int(data[i:i+8],2) for i in range(0,len(data),8) ]).decode())
""" %dat)


"""
遍历目录下所有py文件

:param string dir
    目录名
"""
def walk_dir(dir):
    if not os.path.isdir(dir):
        print("Error: not exists "+dir)
        return
    # 如果存在__pycache__,删除
    pycache_dir = os.path.join(dir,"__pycache__")
    if os.path.isdir(pycache_dir):
        shutil.rmtree(pycache_dir)
    for root,_,file_list in os.walk(dir):
        py_files = list(filter(lambda file_name:str.endswith(file_name,'.py'),file_list))
        if not py_files:
            print("warning: no py files in "+root)
            continue
        for py in py_files:
            py_path = os.path.join(root,py)
            if not os.path.isfile(py_path):
                print("warning: not found "+py_path)
                continue
            bak_py_path = py_path+'.bak' # 在同级目录生成备份
            # 为避免重复加密，以备份是否存在判断
            if os.path.isfile(bak_py_path):
                print("warning: repeat crypt "+py_path)
                continue
            shutil.copy(py_path,bak_py_path)
            make(py_path) #加密
            print("========> crypted "+py_path)
    print('walk dir %s over.' %dir)


def usage():
    print("""
######################################
    python 文件加密
        对指定目录的python文件加密

    usage %s dir [dir1] [dir2]
######################################
    """)

"""
主程序
"""
def main():
    argv = sys.argv
    if len(argv) == 1:
        usage()
        sys.exit()
    else:
        dir_list = argv[1:]
        for dir in dir_list:
            if not os.path.isdir(dir):
                print("Error: "+dir+" is not dir")
                sys.exit(1)
        [ walk_dir(dir) for dir in dir_list ]
        print('complete.')


if __name__ == '__main__':
    main()