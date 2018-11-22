# coding=utf-8
"""
功能：提取URL中所有JPG的超链接，并且下载到指定目录下
input: chaper_url = 'https://www.jianshu.com/p/3703ec3e93ff'
output:save_img(t3, cnt + 1, "D:\Code\Toy_python")
"""
import os
import urllib
from urllib.request import Request
from urllib.request import urlopen  # 用于获取网页

from bs4 import BeautifulSoup  # 用于解析网页


def save_img(img_url, file_name, file_path='book\img'):
    # 保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
    try:
        if not os.path.exists(file_path):
            print('文件夹', file_path, '不存在，重新建立')
            # os.mkdir(file_path)
            os.makedirs(file_path)
        # 获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        # 拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url, filename=filename)
    except IOError as e:
        print('文件操作失败', e)
    except Exception as e:
        print('错误 ：', e)


if __name__ == "__main__":
    # 如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误
    # 主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询

    chaper_url = 'https://www.jianshu.com/p/3703ec3e93ff'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = Request(url=chaper_url, headers=headers)
    html = urlopen(req)

    # html = urlopen('https://www.jianshu.com/p/3703ec3e93ff')
    bsObj = BeautifulSoup(html, 'html.parser')
    t1 = bsObj.find_all('img')
    cnt = 1
    for t2 in t1:
        t3 = t2.get('data-original-src')
        if t3 is not None:
            t3 = "http:" + t3
            print(t3)
            save_img(t3, cnt + 1, "D:\Code\Toy_python")
            cnt = cnt + 1
