# -*- coding: utf-8 -*-
# @Time : 2019/8/27 12:12
# @Author : Max
# @FileName: Constructor.py
# @IDE: PyCharm
from optparse import OptionParser
import os
import codecs

print r"""
 ________     ___    ___ ________  ________  ________  ________  ________  ________      
|\   __  \   |\  \  /  /|\   ____\|\   __  \|\   __  \|\   __  \|\   __  \|\   ____\     
\ \  \|\  \  \ \  \/  / | \  \___|\ \  \|\  \ \  \|\  \ \  \|\  \ \  \|\  \ \  \___|_    
 \ \  \\\  \  \ \    / / \ \  \    \ \  \\\  \ \  \\\  \ \  \\\  \ \  \\\  \ \_____  \   
  \ \  \\\  \  /     \/   \ \  \____\ \  \\\  \ \  \\\  \ \  \\\  \ \  \\\  \|____|\  \  
   \ \_______\/  /\   \    \ \_______\ \_______\ \_______\ \_______\ \_______\____\_\  \ 
    \|_______/__/ /\ __\    \|_______|\|_______|\|_______|\|_______|\|_______|\_________\
             |__|/ \|__|                                                     \|_________|
"""


# [通用] - 遍歷指定文件夾下的所有文件内容
def get_file_names(user_dir):
    file_list = list()

    for root, dirs, files in os.walk(user_dir):
        for f in files:
            file_list.append(f)
    return file_list


# [主程序]
def main(name, type, path):
    file_list = get_file_names(path)

    # 定位文件
    if name is None:
        dealing = file_list[-1]
    else:
        if name in file_list:
            dealing = name
        else:
            print "WARNING: 沒有在文件夾" + str(path) + "找到相關的文件" + str(name)
            exit()

    # 文件處理
    with codecs.open(path, 'r') as subtitles:
        lines = subtitles.readlines()

        with codecs.open(path, 'a+') as output:
            pass


# ---------------------------参数处理------------------------------
parser = OptionParser(usage="usage: %prog [options] filename",
                      version="%prog beta")
parser.add_option("-n", "--name",
                  action="store",  # optional because action defaults to "store"
                  dest="name",
                  default=None,
                  help=u"指定處理的字幕文件, 默認為subtitles文件夾裏的第一個文件", )
parser.add_option("-t", "--type",
                  action="store",  # optional because action defaults to "store"
                  dest="type",
                  default="txt",
                  help=u"指定Constructor處理的字幕文件的類型(ass/str/txt), 默認為txt", )
parser.add_option("-p", "--path",
                  action="store",  # optional because action defaults to "store"
                  dest="path",
                  default="subtitles",
                  help=u"指定字幕文件存放的路徑, 默認為subtitles/下", )
parser.add_option("-o", "--output",
                  action="store",  # optional because action defaults to "store"
                  dest="output",
                  default="artic",
                  help=u"指定整理過的文章存放的路徑, 默認為subtitles/下", )
(options, args) = parser.parse_args()

if __name__ == '__main__':
    main(name=options.name, type=options.type, path=options.path)
