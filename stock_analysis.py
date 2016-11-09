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


now = datetime.datetime.now()
start_date = (now-datetime.timedelta(10)).strftime("%Y-%m-%d")
end_date   = now.strftime("%Y-%m-%d")

# stock_df   = ts.get_hist_data('603060',start_date,end_date)
# print stock_df
# exit()

def REF(data,key,num=0):
    return data.ix[num,key]

stock_code_file = open('stock_code.txt','r')

#sh600000,600000,浦发银行
for line in stock_code_file.readlines():
    # 蜡烛线实体大于当天最高点和最低点差介的一半   ref(open,1)-ref(close,1) > (ref(high,1)-ref(low,1))/2
    # 开盘价格小于等于昨天的收盘价：open<= ref(close,1)
    # 收盘价格大于等昨蜡烛线实体的中部价格 close>= (ref(open,1)-ref(close,1))/2
    stock_arr  = line.split(',')
    stock_code = stock_arr[1]

    print stock_code
    stock_df   = ts.get_hist_data(stock_code,start_date,end_date)
    
    if stock_df.empty or  len(stock_df) < 3:
        continue

    stock_open_1  = REF(stock_df,"open",1)
    stock_close_1 = REF(stock_df,"close",1)
    # 蜡烛实体
    candle_body= stock_open_1 - stock_close_1
    # 蜡烛长度
    candle_len = REF(stock_df,"high",1) - REF(stock_df,"low",1)
    
    stock_open  = REF(stock_df,"open")
    stock_close = REF(stock_df,"close")

    if (stock_open <= stock_close_1) and (stock_close >= (stock_close_1+candle_body/2)) : 
        # print stock_code
        url = "http://image.sinajs.cn/newchart/daily/n/%s.gif"%(stock_arr[0])
        print url
        

stock_code_file.close()



