#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
import csv
import xlrd

import unicodecsv 

def read_csv(filename):                                   #iterators
    with open(filename, 'rb') as f:                       #Rb means opened for reading; b flag changee format of how the files is read.
        reader = unicodecsv.DictReader(f)                 #DictReader means each row would be a dictionary. if data has a header row.
        return list(reader)                               #with: indent all the code_file automatically closed.
                                                          #将迭代器转换为列表的简单方法 list(reader)

enrollments = read_csv('enrollments.csv')                        #create a list and input data
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')
'''


import unicodecsv

enrollments_filename = '/datasets/ud170/udacity-students/enrollments.csv'

## Longer version of code (replaced with shorter, equivalent version below)

# enrollments = []
# f = open(enrollments_filename, 'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
#     enrollments.append(row)
# f.close()

def openfile(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)
    
### Write code similar to the above to load the engagement
### and submission data. The data is stored in files with
### the given filenames. Then print the first row of each
### table to make sure that your code works. You can use the
### "Test Run" button to see the output of your code.

engagement_filename = '/datasets/ud170/udacity-students/daily_engagement.csv'
submissions_filename = '/datasets/ud170/udacity-students/project_submissions.csv'

enrollments = openfile(enrollments_filename)    
daily_engagement = openfile(engagement_filename)     # Replace this with your code
project_submissions = openfile(submissions_filename)  # Replace this with your code

print (enrollments[0])
print (daily_engagement[0])
print (project_submissions[0])
