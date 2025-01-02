
import configparser
import os

config  =   configparser.RawConfigParser()
file= os.path.abspath(os.curdir) +"\\configuaration\\config.ini"



class ReadConfig:
    @staticmethod
    def getURL():
        print(file)
        config.read(file)
        url = config.get('common Info', 'baseURL')
        return url
