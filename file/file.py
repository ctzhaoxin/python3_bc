# -*- coding:utf8 -*-

from django.http import StreamingHttpResponse

from Tools.file.filetype.csvfile import CsvFile
from Tools.file.filetype.excelfile import ExcelFile

class File(object):
    # 定义的文件类型，以及对应的操作类
    __fileType = {
        'csv': 'CsvFile',
        'excel': 'ExcelFile',
    }

    __instance = {}

    """
    # 初始化时，创建文件对象
    """
    def __init__(self, fileType):
        self.key = fileType.lower()
        if self.key not in self.__instance:
            if self.key in self.__fileType:
                 self.__instance[self.key] = eval(self.__fileType[self.key])()
            else:
                print('File init error!!!')
        else:
            pass

    """
    # 读取文件信息
    """
    def read(self, fileName, isHasTitle=True):
        return self.__instance[self.key].read(fileName, isHasTitle)

    """
    # 写入文件信息
    """
    def write(self, data, saveFileName, sheetName='sheet-1', dateIndexList=[], dateFormat='yyyy/mm/dd'):
        self.__instance[self.key].write(data, saveFileName, sheetName='sheet-1', dateIndexList=[], dateFormat='yyyy/mm/dd')
    
    """
    # 上传文件
    """
    def upload(self, fileObj):
        return self.__instance[self.key].upload(fileObj)

    """ 
    # 下载文件
    """
    @classmethod
    def download(self, fileName, exportFileName='export_file'):
        def file_iterator(fileName, chunk_size=512):
            with open(fileName, 'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break

        response = StreamingHttpResponse(file_iterator(fileName))
        response['Content-Type'] = 'application/msexcel'
        response['Content-Disposition'] = 'attachment; filename=%s' % (exportFileName, )

        return response