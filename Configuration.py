# -*- coding: utf-8 -*-
# @Time : 2019/8/27 14:14
# @Author : Max
# @FileName: Configuration.py
# @IDE: PyCharm
import yaml
import sys
import codecs

input_path = None
output_path = None
ending = None
starting = None
remove = None


# ---------------------------通用模塊------------------------------
# [通用] - 顯示數據，添加管道下支持
def write_msg(text):
    sys.stderr.write(text + '\n')


def init(name='Configuration.yml'):
    write_msg("NOTICE: Initialize Configuration")
    global input_path, output_path, ending, starting, remove
    try:
        with codecs.open(name, 'r', errors='ignore') as doc:
            config = yaml.safe_load(doc)
            input_path = config['input']['path']
            output_path = config['output']['path']
            ending = config['input']['sentence']['ending']['re']
            starting = config['input']['sentence']['starting']['re']
            remove = config['input']['sentence']['remove']['re']
    except IOError:
        write_msg("ERROR: Configuration file not found.")
        exit()


if __name__ == '__main__':
    init()
