'''
import os
import csv  #csv处理模块
import xlrd  #处理xls & xlsx文件
import xlwt  #创建xls文件

DATADIR = ""
DATAFILE = "F:\\data\\beatles-diskography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "rb") as f:
        header = f.readline().split(",")  #读取头标区，传入19行
        counter = 0
        for line in f:
            if counter == 10:
                break
            
            fields = line.split(",")      #使用,以切分数据
            entry = {}
            
            for i, value in enumerate(fields):           #使用枚举遍历并存入索引、数据
                entry[header[i].strip()] = value.strip()  #strip()清理空白区域
                
            data.append(entry)
            counter += 1

    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

    
test()
'''


#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    cv = sheet.col_values(1, start_rowx=1, end_rowx=None)

    maxval = max(cv)
    minval = min(cv)

    maxpos = cv.index(maxval) + 1
    minpos = cv.index(minval) + 1

    maxtime = sheet.cell_value(maxpos, 0)
    realtime = xlrd.xldate_as_tuple(maxtime, 0)
    mintime = sheet.cell_value(minpos, 0)
    realmintime = xlrd.xldate_as_tuple(mintime, 0)

    data = {
            'maxtime': realtime,
            'maxvalue': maxval,
            'mintime': realmintime,
            'minvalue': minval,
            'avgcoast': sum(cv) / float(len(cv))
    }
    return data

data = parse_file(datafile)
import pprint
pprint.pprint(data)


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()