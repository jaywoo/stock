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

import datetime,time

html_head = ''' 
<!doctype html>
<html lang="en">
 <head>
  <meta charset="UTF-8">
  <title>%s</title>
  <style>
        .pd10 {padding-top:1px;}
        .fl {float:left}
  </style>
 </head>
 <body>
        <div style="width:1200px;margin:26px auto;padding-bottom:26px;overflow:hidden">
'''
html_end  = '''     
    <div>
 </body>
</html>

'''
url  = "http://image.sinajs.cn/newchart/daily/n/%s.gif"
html_body = '''<div class="pd10 fl">%s<br/><img src="%s"></div>'''

now        = datetime.datetime.now()
start_date = (now-datetime.timedelta(10)).strftime("%Y-%m-%d")
end_date   = now.strftime("%Y-%m-%d")
output_file_path = './'
# stock_code_file = 'stock_code.txt'
stock_code_file = 'stock_code_10'


def REF(data,key,num=0):
    return data.ix[num,key]

