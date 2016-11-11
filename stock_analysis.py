#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
open: 开盘价格
close:收盘价格
high：最高价
low：最低价
volume：成交量
turnover:换手率

ref：ref(open,1) 表示前一天开盘价格

'''

import tushare as ts
import datetime,time
import os
# from functools import partial
import config as conf
# import lib 
import tactics as ttc


def output_stock_code(stock_dict,html_head,html_end):
    for index in stock_dict:
        f_file = conf.output_file_path+"%s_%s.html"%(index,conf.end_date)

        if os.path.isfile(f_file):
            os.remove(f_file)
        f = open(f_file,"ab+")
        f.write(html_head%(index))

        for code_info in stock_dict[index]:
            url  = conf.url%(code_info[0])       
            body = conf.html_body%(code_info[1],url)
            f.write(body)

        f.write(conf.html_end)
        f.close()


stock_code_file = open(conf.stock_code_file,'r')

stock_dict = {}
stock_dict['up_cross_inside_list'] = []

#sh600000,600000,浦发银行
for line in stock_code_file.readlines():
    stock_arr  = line.split(',')
    stock_code = stock_arr[1]

    # print stock_code
    stock_df   = ts.get_hist_data(stock_code,conf.start_date,conf.end_date)
    
    if stock_df.empty or  len(stock_df) < 3:
        continue

    if ttc.up_cross_inside_candle(stock_df) :
        stock_dict['up_cross_inside_list'].append(stock_arr)

stock_code_file.close()
output_stock_code(stock_dict,conf.html_head,conf.html_end)

