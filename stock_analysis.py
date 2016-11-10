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
from functools import partial
import config as conf
import lib 

output_file = conf.output_file%(conf.end_date)
if os.path.isfile(output_file):
    os.remove(output_file)

f = open(output_file,'ab+')
f.write(conf.html_head%(conf.end_date))

stock_code_file = open(conf.stock_code_file,'r')

#sh600000,600000,浦发银行
for line in stock_code_file.readlines():
    # 蜡烛线实体大于当天最高点和最低点差介的一半   ref(open,1)-ref(close,1) > (ref(high,1)-ref(low,1))/2
    # 开盘价格小于等于昨天的收盘价：open<= ref(close,1)
    # 收盘价格大于等昨蜡烛线实体的中部价格 close>= (ref(open,1)-ref(close,1))/2
    stock_arr  = line.split(',')
    stock_code = stock_arr[1]

    # print stock_code
    stock_df   = ts.get_hist_data(stock_code,conf.start_date,conf.end_date)
    
    if stock_df.empty or  len(stock_df) < 3:
        continue

    stock_df.ref =  partial(lib.ref, stock_df)
    open_1  = stock_df.ref("open",1)
    close_1 = stock_df.ref("close",1)
    high_1 = stock_df.ref("high",1)
    low_1  = stock_df.ref("low",1)
    # 蜡烛实体
    candle_body_1 = open_1 - close_1
    # 蜡烛长度
    candle_len_1 = high_1 - low_1
    
    stock_open  = stock_df.ref("open")
    stock_close = stock_df.ref("close")

    ''' 
        向上刺透形态
            1.前一天实体占线的一半以上 ： (open-close) >= (high - low )/2 
            2.当天开盘价小于等于前一天收盘价
            3.收盘价在前一天实体1/2处或以上 close > (ref(open,1)+ref(close,1))/2
    '''
    
    if ( candle_body_1 >= candle_len_1/2 and stock_open <= close_1 and  stock_close >= (open_1+close_1)/2 ): 
        print stock_code
        url  = conf.url%(stock_arr[0])
        body = conf.html_body%(url)
        f.write(body)
        
f.write(conf.html_end)
stock_code_file.close()
f.close()


