# -*- coding:utf8 -*-

import csv

from Tools.file.interface.ifile import IFile

class CsvFile(IFile):

    """
    # 读取csv文件数据
    # @params   string  fileName    要读取的csv文件名
    # @params   bool    isHasTitle  文件中是否有title
    #
    # @return   list    dataList    从文件中读取的数据
    """
    def read(self, fileName, isHasTitle=True):
        dataList = []
        with open(fileName, 'r') as fp:
            reader = csv.reader(fp)
            for data in reader:
                if isHasTitle:
                    isHasTitle = False
                    continue
                
                dataList.append(data)
        
        return dataList
    
    def write(self, data):
        print('CsvFile write')