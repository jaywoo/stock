#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lib
from functools import partial

# 向上刺透形态
def up_cross_inside_candle(stock_df):
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
        向上刺透形态,超过前天实体就算是包线了
            1.前一天实体占线的一半以上 ： (open-close) >= (high - low )/2 
            2.当天开盘价小于等于前一天收盘价
            3.收盘价在前一天实体1/2处或以上 close > (ref(open,1)+ref(close,1))/2
    '''
    if ( candle_body_1 >= candle_len_1/2 and 
        stock_open <= close_1*1.005 and  
        stock_close >= (open_1+close_1)/2 and 
        stock_close <= high_1): 
        return True
    return False



