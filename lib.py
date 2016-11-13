#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import math

def ref(data,key,num=0):
    return data.ix[num,key]

# 获取days个工作日前的日期
def get_work_date(days,now = datetime.datetime.now()):
    # 计算天数=周末数*2+days 
    counts = math.ceil((days-now.weekday())/5.0)*2+days
    return now - datetime.timedelta(counts)
