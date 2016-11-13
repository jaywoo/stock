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
import lib
import tactics

def output_stock_code(stock_dict,html_head,html_end):
    pre = 'sz'
    for index in stock_dict:
        if not stock_dict[index]:
            continue

        f_file = conf.output_file_path+"%s_%s.html"%(index,conf.end_date)

        if os.path.isfile(f_file):
            os.remove(f_file)
        f = open(f_file,"ab+")
        f.write(html_head%(index))

        for code in stock_dict[index]:
            if code[0] == 6:
                pre = 'sh'
            url  = conf.daily_url%(pre+code)       
            body = conf.html_body%(code,url)
            f.write(body)

        f.write(conf.html_end)
        f.close()

def main():
    stock_dict = {}
    stock_dict['up_cross_inside_list'] = []
    days = 21
    start_date = lib.get_work_date(days).strftime("%Y-%m-%d")
    stock_basics = ts.get_stock_basics()
    for code,stock in stock_basics.iterrows():
        print code
        df = ts.get_hist_data(code,start_date)
        if df.empty or  len(df) < 3:
            continue
        if tactics.up_cross_inside_candle(df) :
            stock_dict['up_cross_inside_list'].append(code)
            break;

    output_stock_code(stock_dict,conf.html_head,conf.html_end)


if __name__ == '__main__':
    main()
    # end_date = datetime.datetime(2016,9, 27, 23, 9, 12, 946118)
    # start_date = lib.get_work_date(5,end_date).strftime('%Y-%m-%d')
    # df = ts.get_hist_data('000599',start_date,end_date.strftime('%Y-%m-%d'))
    
    # print tactics.up_cross_inside_candle(df)
    # print lib.get_work_date(5).strftime("%Y-%m-%d")
    # print lib.get_work_date(6).strftime("%Y-%m-%d")
    # print lib.get_work_date(12).strftime("%Y-%m-%d")
    # print lib.get_work_date(13).strftime("%Y-%m-%d")
    # print lib.get_work_date(21).strftime("%Y-%m-%d")
