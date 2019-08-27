# -*- coding: utf-8 -*-
# @Time : 2019/8/27 14:14
# @Author : Max
# @FileName: Configuration.py
# @IDE: PyCharm
import yaml
import sys
import codecs


# ---------------------------通用模塊------------------------------
# [通用] - 顯示數據，添加管道下支持
def write_msg(text):
    sys.stderr.write(text + '\n')


def init(name = 'Configuration.yml'):
    write_msg("NOTICE: Initialize Configuration")
    try:
        with codecs.open(name, 'r', errors='ignore') as config:
            pass
    except IOError:
        write_msg("ERROR: Configuration file not found.")
        exit()
