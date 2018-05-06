# coding=utf-8
import os

path = "/Users/ifind/Desktop/python/";
os.chdir( path )

filesName = os.listdir()
for name in filesName:
    os.rename( name, "[备份]" + name )
