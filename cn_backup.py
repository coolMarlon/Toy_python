# coding=utf-8
"""
功能：通过CNBLog导出的xml在本地备份文件生成单个文件
input: dom = xml.dom.minidom.parse('C:\\Users\\shish\\Desktop\\back.xml') 指明了本地文件的位置
output:在当前文件夹的同即目录有一个xxxnew文件夹，里面储存了每一个md文件
"""
import xml.dom.minidom

import os


def txt(name, text):  # 定义函数名
    b = os.getcwd()[:-4] + 'new\\'

    if not os.path.exists(b):  # 判断当前路径是否存在，没有则创建new文件夹
        os.makedirs(b)

    xxoo = b + name + '.md'  # 在当前py文件所在路径下的new文件中创建txt

    file = open(xxoo, 'w',encoding="utf-8")

    file.write(text)  # 写入内容信息

    file.close()
    print('ok')


if __name__ == "__main__":
    # txt("errorindex-pack died of signal fatal index-pack failed【Git】","456")
    dom = xml.dom.minidom.parse('C:\\Users\\shish\\Desktop\\back.xml')
    root = dom.documentElement
    bb = root.getElementsByTagName('description')
    tt = root.getElementsByTagName('title')
    for i in range(1,79):
        b = bb[i]
        t = tt[i]
        # print(type(t.firstChild.data))
        try:
            txt(t.firstChild.data,b.firstChild.data)
        except:
            pass
        # print(b.firstChild.data)
        # print(t.firstChild.data)