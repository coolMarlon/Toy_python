# -*- coding: utf-8 -*-
import jieba

import xlrd as xlrd
import xlwt

f = xlwt.Workbook()

# 创建一个sheet，cell_overwrite_ok默认为False，当设置为True时，覆盖已有数据不会报错
sheet1 = f.add_sheet('Sheet1', cell_overwrite_ok=False)

readbook = xlrd.open_workbook(r'source.xlsx')

# 名字的方式
sheet = readbook.sheet_by_name('Sheet1')

nrows = sheet.nrows  # 行
ncols = sheet.ncols  # 列

# 复制第一行
for i in range(0, ncols):
    sheet1.write(0, i, label=sheet.cell(0, i).value)

for i in range(1, nrows):
    word = sheet.cell(i, 1).value
    cut_word = jieba.cut(word)
    sheet1.write(i, 1, label=sheet.cell(i, 1).value)
    sheet1.write(i, 2, label=(", ".join(cut_word)))

f.save('cut_word.xls')
