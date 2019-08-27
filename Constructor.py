# -*- coding: gbk -*-
# @Time : 2019/8/27 12:12
# @Author : Max
# @FileName: Constructor.py
# @IDE: PyCharm
from optparse import OptionParser
import os
import codecs
import sys

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


# ---------------------------通用模塊------------------------------
# [通用] - 遍歷指定文件夾下的所有文件内容
def get_file_names(user_dir):
    file_list = list()

    for root, dirs, files in os.walk(user_dir):
        for f in files:
            file_list.append(f)
    return file_list


# [通用] - 創建指定名稱的文件夾/路徑
def mk_dir(dir_path):
    is_exist = os.path.exists(dir_path)
    if not is_exist:
        os.makedirs(dir_path)
        print("NOTICE: folder " + dir_path + " was created.")
        return True
    else:
        return False


# [通用] - 顯示數據，添加管道下支持
def write_msg(text):
    sys.stderr.write(text + '\n')


# ---------------------------主程序---------------------------------
def main(name, type, input, output):
    file_list = get_file_names(input)
    dealing = None
    # 定位文件
    if name is None:
        dealing = file_list[-1]
    else:
        if name in file_list:
            dealing = name
        else:
            write_msg("ERROR: 沒有找到相關的文件" + input + "\\" + str(name))
            exit()

    # 文件處理
    with codecs.open(input + "\\" + dealing, 'r') as subtitles:
        lines = subtitles.readlines()
        for line in lines:
            # 如果當前語句的長度>=2 這説明不是空行
            if len(line) >= 2:
                ending = line[-2]
                if ending != ',' and '.' and ':' and '?':
                    pass

            # 移除空行
            else:
                del line
            # 語句處理

    # 輸出文章
    mk_dir(output)
    with codecs.open(output + "\\" + dealing, 'a+') as article:
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
parser.add_option("-i", "--input",
                  action="store",  # optional because action defaults to "store"
                  dest="input",
                  default="subtitles",
                  help=u"指定輸入的字幕文件存放的路徑, 默認為subtitles/下", )
parser.add_option("-o", "--output",
                  action="store",  # optional because action defaults to "store"
                  dest="output",
                  default="article",
                  help=u"指定輸出的整理過的文章存放的路徑, 默認為subtitles/下", )
(options, args) = parser.parse_args()

if __name__ == '__main__':
    main(name=options.name, type=options.type, input=options.input, output=options.output)
