#!/usr/bin/python
import sys
import os


class Constants:


    def __init__(self):
        self.__OK = 0
        self.__FAIL = 1
        self.__ERROR = -1
        self.__NODATA = 100
        self.__GLOBALCONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)),"config","globalConfig.properties")
        

    @property
    def OK(self):

        return self.__OK

    @property
    def ERROR(self):

        return self.__ERROR

    @property
    def NODATA(self):
        return self.__NODATA

    @property
    def FAIL(self):

        return self.__FAIL

    @property
    def GLOBALCONFIG(self):

        return self.__GLOBALCONFIG
