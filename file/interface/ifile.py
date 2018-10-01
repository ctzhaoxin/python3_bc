# -*- coding:utf-8 -*-

import os
from abc import ABCMeta, abstractmethod

from django.conf import settings



class IFile(metaclass=ABCMeta):

    # read file content
    @abstractmethod
    def read(self):
        pass
    
    # write to file
    @abstractmethod
    def write(self):
        pass

    """
    # 上传文件 
    """
    @classmethod
    def upload(self, fileObj):
        # 保存文件的名称
        fileName = os.path.join(settings.BASE_DIR, 'upload/', fileObj.name)
        fp = open(fileName, 'wb')
        for data in fileObj.chunks():
            fp.write(data)
        
        return fileName