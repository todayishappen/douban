import xlwt

# 关于excel表
'''
workbook=xlwt.Workbook(encoding="utf-8") #创建Workbook对象
worksheet=workbook.add_sheet('sheet1')
worksheet.write(0,0,"hello") #表示在第一行第一列放入内容 【在内存中】
workbook.save('student.xls')
'''

workbook=xlwt.Workbook(encoding="utf-8") #创建Workbook对象
worksheet=workbook.add_sheet('sheet1')
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d =%d"%(i+1,j+1,(i+1)*(j+1)))
workbook.save('student.xls')