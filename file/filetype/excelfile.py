# -*- coding:utf8 -*-

import xlwt

from Tools.file.interface.ifile import IFile

class ExcelFile(IFile):

    def read(self, filename):
        print('ExcelFile read')
    
    """
    # Excel 数据写入
    # @params   list    data    写入Excel的数据
    # @params   string  saveFileName    生成的Excel文件的名称
    # @params   string  sheetName       sheet的名称，默认只有一个sheet
    # @params   list    dateIndexList   写入Excel，中日期的字段的索引， 从0开始
    # @params   string  dateFormat      日期格式字符串
    """
    def write(self, data, saveFileName, sheetName='sheet-1', dateIndexList=[], dateFormat='yyyy/mm/dd'):
        wbk = xlwt.Workbook()
        sheet1 = wbk.add_sheet(sheetName, cell_overwrite_ok=True)

        # 日期格式
        if dateIndexList:
            pass
        else:
            dateFormatObj = xlwt.XFStyle()
            dateFormatObj.num_format_str = dateFormat

        for i in range(len(data)):
            for j in range(len(data[0])):
                if j in dateIndexList:
                    dateFloat = xlrd.xldate_as_tuple(data[i][j], 0)
                    sheet1.write(i, j, datetime(*dateFloat), dateFormatObj)
                else:
                    sheet1.write(i, j, str(data[i][j]))
        
        wbk.save(saveFileName)
