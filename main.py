# -*- coding: utf-8 -*-
# @Time        : 2022/7/26 10:37
# @Author      : martin_wang
# @FileName    : hist.py
# @IDE         : PyCharm
# @Description :
import os
import re

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import random
import matplotlib

import numpy as np
import matplotlib.pyplot as plt
import random

from config import settings

# 准备数据
x_data = [f"20{i}年" for i in range(17, 23)]
y_data = [45.4, 80.1, 147.7, 278.9, 544.9, 586.0]
y1_data = [63, 120, 168, 195, 344, 1035]

figure = {}
# 正确显示中文和负号
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


# f = plt.figure()
# 画图，plt.bar()可以画柱状图
#
# plt.bar(x_data, y_data)
#
# # 设置图片名称
# plt.title("2017-2022年中国VR/AR市场规模及预测趋势图")
# # 设置x轴标签名
# plt.xlabel("年份")
# # 设置y轴标签名
# plt.ylabel("市场规模/亿元")
# # 显示
#
# ax = plt.axes()
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
#
# plt.show()

def barh_plot(x_ticks, y_data, x_label, y_label, title):
    fig = plt.figure()

    x_ticks = list(reversed(x_ticks))
    y_data = list(reversed(y_data))

    ax = fig.add_subplot(111)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.barh(x_ticks, y_data)
    # 设置图片名称
    plt.title(title)
    # 设置x轴标签名
    plt.xlabel(x_label)
    # 设置y轴标签名
    plt.ylabel(y_label)
    # 显示
    pattern = re.compile(r"[\/\\\:\*\?\"\<\>\|]")  # '/ \ : * ? " < > |'
    title = re.sub(pattern, "_", title)  # 替换为下划线

    plt.savefig(os.path.join('images', r'{}.svg'.format(title)))


def bar_plot(x_ticks, y_data, x_label, y_label, title):
    fig = plt.figure()

    ax = fig.add_subplot(111)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.bar(x_ticks, y_data)

    # 设置图片名称
    plt.title(title)
    # 设置x轴标签名
    plt.xlabel(x_label)
    # 设置y轴标签名
    plt.ylabel(y_label)
    # 显示
    pattern = re.compile(r"[\/\\\:\*\?\"\<\>\|]")  # '/ \ : * ? " < > |'
    title = re.sub(pattern, "_", title)  # 替换为下划线

    plt.savefig(os.path.join('images', r'{}.svg'.format(title)))


def twinx_bar_plot(x_ticks, y1_data, y2_data, x_label, y1_label, y2_label, title):
    width = 0.4
    fig = plt.figure()

    ax1 = fig.add_subplot(111)
    ax1.bar(np.arange(len(y1_data)), y1_data, color='tomato', width=width, label='投资数量')

    ax2 = ax1.twinx()
    ax2.bar(np.arange(len(y2_data)) + width, y2_data, color='steelblue', width=width, label='投资金额')

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y1_label)
    ax1.spines['top'].set_visible(False)
    ax2.set_ylabel(y2_label)
    ax2.spines['top'].set_visible(False)
    # 设置图片名称
    plt.title(title)
    plt.xticks(np.arange(len(x_ticks)) + width / 2, x_ticks)

    # 保存
    pattern = re.compile(r"[\/\\\:\*\?\"\<\>\|]")  # '/ \ : * ? " < > |'
    title = re.sub(pattern, "_", title)  # 替换为下划线
    plt.savefig(os.path.join('images', r'{}.svg'.format(title)))

    plt.show()


def pie_plot(x_data, labels, explode, title):
    plt.figure()

    # 设置每一块分割出的间隙大小
    plt.pie(x_data, explode=explode, labels=labels, autopct='%1.2f%%', startangle=180)
    plt.title(title)  # 设置标题

    pattern = re.compile(r"[\/\\\:\*\?\"\<\>\|]")  # '/ \ : * ? " < > |'
    title = re.sub(pattern, "_", title)  # 替换为下划线

    plt.savefig(os.path.join('images', r'{}.svg'.format(title)))
    plt.show()


# for pie in settings.get('pies'):
#     print(pie.get('explode'))
#     pie_plot(pie.get('x_data'), pie.get('labels'), eval(pie.get('explode')), pie.get('title'))
if __name__ == '__main__':
    for i in settings.get('barhs'):
        barh_plot(i.get('x_ticks'), i.get('y_data'), i.get('x_label'), i.get('y_label'), i.get('title'))

    for i in settings.get('twinx_bars'):
        twinx_bar_plot(i.get('x_ticks'), i.get('y1_data'), i.get('y2_data'), i.get('x_label'), i.get('y1_label'),
                       i.get('y2_label'), i.get('title'))
