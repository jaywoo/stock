#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
open: 开盘价格
close:收盘价格
high：最高价
low：最低价
ref：ref(open,1) 表示前一天开盘价格

'''

import tushare as ts
import datetime,time

now = datetime.datetime.now()
start_date = now.strftime("%Y-%m-%d")
end_date   = (now-datetime.timedelta(1)).strftime("%Y-%m-%d")

stock_code_file = open('stock_code.txt','r')
#sh600000,600000,浦发银行
for line in stock_code_file.readlines():
    # 蜡烛线实体大于当天最高点和最低点差介的一半   ref(open,1)-ref(close,1) > (ref(high,1)-ref(low,1))/2
    # 开盘价格小于等于昨天的收盘价：open<=close-1
    # 收盘价格大于等昨蜡烛线实体的中部价格 close>= (ref(open,1)-ref(close,1))/2
    stock_code = line.split(',')[1]

    
stock_code_file.close()



