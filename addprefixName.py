# coding=utf-8
"""
功能：给定一个目录名，*srcdir*，给此目录下所有文件(文件夹也包括，非递归)添加一个前缀(该文件的创建时间)，格式为yyyy-mm-dd-
"""

import sys, string, os, shutil
import time

def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    # return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)
    return time.strftime('%Y-%m-%d-',timeStruct)


if __name__ == "__main__":
    srcdir = "E:\\SomeFiles\\Test"
    srcfiles = os.listdir(srcdir)
    print(srcfiles)
    for srcfile in srcfiles:
        dirPath = os.path.join(srcdir, srcfile)
        destfile = srcdir + "\\" + (TimeStampToTime(os.path.getctime(dirPath)))+srcfile
        os.rename(dirPath, destfile)


