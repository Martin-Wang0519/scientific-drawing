# -*- coding: utf-8 -*-
# @Time        : 2022/4/26 9:52
# @Author      : martin_wang
# @FileName    : test2.py
# @IDE         : PyCharm
# @Description : 配置文件解析

import os
import copy
import traceback
import yaml


class YamlParse(object):
    def __init__(self, yaml_path):
        self.yaml_path = yaml_path
        self.opts = self.get_yaml()

    def get_yaml(self):
        """
        解析 yaml
        :return: s  字典
        """
        path = self.yaml_path
        try:
            with open(path, 'r', encoding='utf-8') as file:
                config = yaml.safe_load(file)
                # config = yaml.load(file, Loader=yaml.Loader)
            return config
        except Exception as exception:
            print(traceback.format_exc())
        return None

    def set(self, key, value):
        """ 通过 key 设置某一项值 """
        self.opts[key] = value

    def get(self, key, default=None):
        """ 通过 key 获取值 """
        return self.opts.get(key, default)

    def copy(self):
        """ 复制配置 """
        return copy.deepcopy(self.opts)

    def update(self, new_opts):
        """ 全部替换配置 """
        self.opts.update(new_opts)

    def print(self):
        print(self.opts)


datas = YamlParse('data.yaml')

if __name__ == '__main__':
    pass

