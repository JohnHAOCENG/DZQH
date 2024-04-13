
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:58:09 2020

@author: thinker
"""
#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的
get_ipython().run_line_magic('matplotlib', 'auto')
from dateutil import rrule
import datetime
import calendar
import pymysql.cursors
import math
from scipy import stats

# # 参数设置

# In[2]:


# 函数日期：月度调整
import datetime
import math

def date_shift_month(date,shift_month_num):  #date为str格式，如"2020-9-7",；shift_month_mun为数字，负数代表向前推N月
    date = datetime.datetime.strptime(date,'%Y-%m-%d').date() #将str日期格式转换成date格式
    year = date.year
    month = date.month
    day = date.day
    a = year*12+month+shift_month_num
    return datetime.date(math.floor(a/12),a%12,day) #获取日期后并转换成str格式


# In[3]:


# 截止时间设置 格式需为：YYYY-MM-DD
end_date =datetime.datetime.strptime('2024-03-22','%Y-%m-%d')#截止日期
now_month = datetime.datetime.strptime('2024-03-01','%Y-%m-%d')#当月
# 业绩区间日期列表
one_week_date =datetime.datetime.strptime('2024-03-15','%Y-%m-%d') 
one_month_date =datetime.datetime.strptime('2024-02-23','%Y-%m-%d')#春节少一天
three_month_date = datetime.datetime.strptime('2023-12-22','%Y-%m-%d')
six_month_date = datetime.datetime.strptime('2023-09-22','%Y-%m-%d')
one_year_date = datetime.datetime.strptime('2023-03-24','%Y-%m-%d')
three_year_date = datetime.datetime.strptime('2021-03-19','%Y-%m-%d')  

year_to_date = datetime.datetime.strptime('2024-01-01','%Y-%m-%d')
year_start_date_2023 =datetime.datetime.strptime("2023-01-01",'%Y-%m-%d') 
year_end_date_2023 =datetime.datetime.strptime("2023-12-31",'%Y-%m-%d')   
year_start_date_2022 =datetime.datetime.strptime("2022-01-01",'%Y-%m-%d') 
year_end_date_2022 =datetime.datetime.strptime("2022-12-31",'%Y-%m-%d')  
year_start_date_2021 =datetime.datetime.strptime("2021-01-01",'%Y-%m-%d') 
year_end_date_2021 =datetime.datetime.strptime("2021-12-31",'%Y-%m-%d')  
year_start_date_2020 =datetime.datetime.strptime("2020-01-01",'%Y-%m-%d') 
year_end_date_2020 =datetime.datetime.strptime("2020-12-31",'%Y-%m-%d')  
year_start_date_2019 =datetime.datetime.strptime("2019-01-01",'%Y-%m-%d') 
year_end_date_2019 =datetime.datetime.strptime("2019-12-31",'%Y-%m-%d')  
year_start_date_2018 =datetime.datetime.strptime("2018-01-01",'%Y-%m-%d')  
year_end_date_2018 = datetime.datetime.strptime("2018-12-31",'%Y-%m-%d') 
year_start_date_2017 =datetime.datetime.strptime("2017-01-01",'%Y-%m-%d')  
year_end_date_2017 =datetime.datetime.strptime("2017-12-31",'%Y-%m-%d')  
year_start_date_2016 =datetime.datetime.strptime("2016-01-01",'%Y-%m-%d')  
year_end_date_2016 = datetime.datetime.strptime("2016-12-31",'%Y-%m-%d') 
year_start_date_2015 =datetime.datetime.strptime("2015-01-01",'%Y-%m-%d')  
year_end_date_2015 = datetime.datetime.strptime("2015-12-31",'%Y-%m-%d') 
year_start_date_2014 =datetime.datetime.strptime("2014-01-01",'%Y-%m-%d')  
year_end_date_2014 = datetime.datetime.strptime("2014-12-31",'%Y-%m-%d') 
year_start_date_2013 =datetime.datetime.strptime("2013-01-01",'%Y-%m-%d')  
year_end_date_2013 = datetime.datetime.strptime("2013-12-31",'%Y-%m-%d') 
jan_start_date = datetime.datetime.strptime("2024-01-01",'%Y-%m-%d')
jan_end_date = datetime.datetime.strptime("2024-01-31",'%Y-%m-%d')
feb_start_date = datetime.datetime.strptime("2024-02-01",'%Y-%m-%d')
feb_end_date = datetime.datetime.strptime("2024-02-29",'%Y-%m-%d')
mar_start_date = datetime.datetime.strptime("2024-03-01",'%Y-%m-%d')
mar_end_date = datetime.datetime.strptime("2024-03-31",'%Y-%m-%d')#每次更新到
apr_start_date = datetime.datetime.strptime("2024-04-01",'%Y-%m-%d')
apr_end_date = datetime.datetime.strptime("2024-04-03",'%Y-%m-%d')
may_start_date = datetime.datetime.strptime("2024-05-01",'%Y-%m-%d')
may_end_date = datetime.datetime.strptime("2024-05-31",'%Y-%m-%d')
jun_start_date = datetime.datetime.strptime("2024-06-01",'%Y-%m-%d')
jun_end_date = datetime.datetime.strptime("2024-06-30",'%Y-%m-%d')
jul_start_date = datetime.datetime.strptime("2024-07-01",'%Y-%m-%d')
jul_end_date = datetime.datetime.strptime("2024-07-28",'%Y-%m-%d')
aug_start_date = datetime.datetime.strptime("2024-08-01",'%Y-%m-%d')
aug_end_date = datetime.datetime.strptime("2024-08-31",'%Y-%m-%d')
sep_start_date = datetime.datetime.strptime("2024-09-01",'%Y-%m-%d')
sep_end_date = datetime.datetime.strptime("2024-09-30",'%Y-%m-%d')
oct_start_date = datetime.datetime.strptime("2024-10-01",'%Y-%m-%d')
oct_end_date = datetime.datetime.strptime("2024-10-27",'%Y-%m-%d')
nov_start_date = datetime.datetime.strptime("2024-11-01",'%Y-%m-%d')
nov_end_date = datetime.datetime.strptime("2024-11-30",'%Y-%m-%d')
dec_start_date = datetime.datetime.strptime("2024-12-01",'%Y-%m-%d')
dec_end_date = datetime.datetime.strptime("2024-12-29",'%Y-%m-%d')
l_jan_start_date = datetime.datetime.strptime("2023-01-01",'%Y-%m-%d')
l_jan_end_date = datetime.datetime.strptime("2023-01-31",'%Y-%m-%d')
l_feb_start_date = datetime.datetime.strptime("2023-02-01",'%Y-%m-%d')
l_feb_end_date = datetime.datetime.strptime("2023-02-28",'%Y-%m-%d')
l_mar_start_date = datetime.datetime.strptime("2023-03-01",'%Y-%m-%d')
l_mar_end_date = datetime.datetime.strptime("2023-03-31",'%Y-%m-%d')
l_apr_start_date = datetime.datetime.strptime("2023-04-01",'%Y-%m-%d')
l_apr_end_date = datetime.datetime.strptime("2023-04-30",'%Y-%m-%d')
l_may_start_date = datetime.datetime.strptime("2023-05-01",'%Y-%m-%d')
l_may_end_date = datetime.datetime.strptime("2023-05-31",'%Y-%m-%d')
l_jun_start_date = datetime.datetime.strptime("2023-06-01",'%Y-%m-%d')
l_jun_end_date = datetime.datetime.strptime("2023-06-30",'%Y-%m-%d')
l_jul_start_date = datetime.datetime.strptime("2023-07-01",'%Y-%m-%d')
l_jul_end_date = datetime.datetime.strptime("2023-07-30",'%Y-%m-%d')
l_aug_start_date = datetime.datetime.strptime("2023-08-01",'%Y-%m-%d')
l_aug_end_date = datetime.datetime.strptime("2023-08-25",'%Y-%m-%d')
l_sep_start_date = datetime.datetime.strptime("2023-09-01",'%Y-%m-%d')
l_sep_end_date = datetime.datetime.strptime("2023-09-30",'%Y-%m-%d')
l_oct_start_date = datetime.datetime.strptime("2023-10-01",'%Y-%m-%d')
l_oct_end_date = datetime.datetime.strptime("2023-10-31",'%Y-%m-%d')
l_nov_start_date = datetime.datetime.strptime("2023-11-01",'%Y-%m-%d')
l_nov_end_date = datetime.datetime.strptime("2023-11-30",'%Y-%m-%d')
l_dec_start_date = datetime.datetime.strptime("2023-12-01",'%Y-%m-%d')
l_dec_end_date = datetime.datetime.strptime("2023-12-31",'%Y-%m-%d')

return_start_date_list = [one_week_date,now_month,one_month_date,three_month_date,six_month_date,one_year_date,three_year_date,year_to_date,year_start_date_2023,year_start_date_2022,year_start_date_2021,year_start_date_2020,year_start_date_2019,year_start_date_2018,year_start_date_2017,year_start_date_2016]
return_end_date_list = [end_date,end_date,end_date,end_date,end_date,end_date,end_date,end_date,year_end_date_2023,year_end_date_2022,year_end_date_2021,year_end_date_2020,year_end_date_2019,year_end_date_2018,year_end_date_2017,year_end_date_2016]
return_start_end_date = pd.DataFrame([return_start_date_list,return_end_date_list],index=["开始日期","结束日期"]).T
return_start_end_date.index=["近一周","当月收益","近一月","近三月","近六月","近一年","近三年","今年以来","2023年","2022年","2021年","2020年","2019年","2018年","2017年","2016年"]
return_start_end_date

#最大回撤时间列表
MaxDrawdown_start_date_list = [year_to_date,year_start_date_2023,year_start_date_2022,year_start_date_2021,year_start_date_2020,year_start_date_2019,year_start_date_2018,year_start_date_2017,year_start_date_2016]
MaxDrawdown_end_date_list = [end_date,year_end_date_2023,year_end_date_2022,year_end_date_2021,year_end_date_2020,year_end_date_2019,year_end_date_2018,year_end_date_2017,end_date]
MaxDrawdown_start_end_date = pd.DataFrame([MaxDrawdown_start_date_list,MaxDrawdown_end_date_list],index=["开始日期","结束日期"]).T
MaxDrawdown_start_end_date.index=["今年以来最大回撤","2023年最大回撤","2022年最大回撤","2021年最大回撤","2020年最大回撤","2019年最大回撤","2018年最大回撤","2017年最大回撤","2016年以来最大回撤"]
MaxDrawdown_start_end_date
#MaxDrawdown_start_end_date

#Sharpe时间列表 区间年化收益法
Sharpe_i_start_date_list = [year_to_date]
Sharpe_i_end_date_list = [end_date]
Sharpe_i_start_end_date = pd.DataFrame([Sharpe_i_start_date_list,Sharpe_i_end_date_list],index=["开始日期","结束日期"]).T
Sharpe_i_start_end_date.index=["今年以来Sharpe"]

#Sharpe时间列表
Sharpe_start_date_list = [year_to_date,year_start_date_2013]
Sharpe_end_date_list = [end_date,end_date]
Sharpe_start_end_date = pd.DataFrame([Sharpe_start_date_list,Sharpe_end_date_list],index=["开始日期","结束日期"]).T
Sharpe_start_end_date.index=["今年以来Sharpe","2013年以来Sharpe"]

#年化收益时间列表 平均年化
Annual_Return_m_start_date_list = [year_to_date,year_start_date_2013]
Annual_Return_m_end_date_list = [end_date,end_date]
Annual_Return_m_start_end_date = pd.DataFrame([Annual_Return_m_start_date_list,Annual_Return_m_end_date_list],index=["开始日期","结束日期"]).T
Annual_Return_m_start_end_date.index=["今年以来年化收益_平均","2013年以来年化收益_平均"]

#年化收益时间列表 区间年化
Annual_Return_i_start_date_list = [year_to_date,year_start_date_2016]
Annual_Return_i_end_date_list = [end_date,end_date]
Annual_Return_i_start_end_date = pd.DataFrame([Annual_Return_i_start_date_list,Annual_Return_i_end_date_list],index=["开始日期","结束日期"]).T
Annual_Return_i_start_end_date.index=["今年以来年化收益_区间","2016年以来年化收益_区间"]

#年化波动时间列表
Annual_Volatility_start_date_list = [year_to_date,year_start_date_2013]
Annual_Volatility_end_date_list = [end_date,end_date]
Annual_Volatility_start_end_date = pd.DataFrame([Annual_Volatility_start_date_list,Annual_Volatility_end_date_list],index=["开始日期","结束日期"]).T
Annual_Volatility_start_end_date.index=["今年以来年化波动","2013年以来年化波动"]

#月度收益时间列表 每月新增
Mongthly_Return_start_date_list = [jan_start_date,feb_start_date,mar_start_date,apr_start_date,may_start_date,jun_start_date,jul_start_date,aug_start_date,sep_start_date,oct_start_date,nov_start_date,dec_start_date,l_jan_start_date,l_feb_start_date,l_mar_start_date,l_apr_start_date,l_may_start_date,l_jun_start_date,l_jul_start_date,l_aug_start_date,l_sep_start_date,l_oct_start_date,l_nov_start_date,l_dec_start_date]
Mongthly_Return_end_date_list = [jan_end_date,feb_end_date,mar_end_date,apr_end_date,may_end_date,jun_end_date,jul_end_date,aug_end_date,sep_end_date,oct_end_date,nov_end_date,dec_end_date,l_jan_end_date,l_feb_end_date,l_mar_end_date,l_apr_end_date,l_may_end_date,l_jun_end_date,l_jul_end_date,l_aug_end_date,l_sep_end_date,l_oct_end_date,l_nov_end_date,l_dec_end_date]
Mongthly_Return_start_end_date = pd.DataFrame([Mongthly_Return_start_date_list,Mongthly_Return_end_date_list],index=["开始日期","结束日期"]).T
Mongthly_Return_start_end_date.index=["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月","2023年1月","2023年2月","2023年3月","2023年4月","2023年5月","2023年6月","2023年7月","2023年8月","2023年9月","2023年10月","2023年11月","2023年12月"]

return_start_end_date


# # 产品列表与代码

# In[4]:


# 私募重点跟踪池数据导入
fund_info = pd.read_excel(r'C:\Users\zhc12\Desktop\基金评价\周报\周报数据\重点跟踪池.xlsx',"重点")


# 重点关注产品数据
fund_info_guanzhu = fund_info[(fund_info["是否存续"] == 0)]
fund_info_guanzhu = fund_info_guanzhu[["朝阳永续代码","私募机构","核心人物","最新规模","产品名称","成立日期","大类策略","细分策略1","细分策略2","是否存续","是否自营"]]
fund_info_guanzhu["朝阳永续代码"] = round(fund_info_guanzhu[["朝阳永续代码"]],0).astype(str)
fund_info_guanzhu.set_index("朝阳永续代码",inplace = True)
fund_info_guanzhu


# 国盛存续产品数据
fund_info_cunxu = fund_info[(fund_info["是否存续"] == 1)]
fund_info_cunxu = fund_info_cunxu[["朝阳永续代码","私募机构","核心人物","最新规模","产品名称","成立日期","大类策略","细分策略1","细分策略2","是否存续","是否自营"]]
fund_info_cunxu["朝阳永续代码"] = fund_info_cunxu[["朝阳永续代码"]].astype(str)
fund_info_cunxu.set_index("朝阳永续代码",inplace = True)

# 组合投资续产品数据
fund_info_zuhe = fund_info[(fund_info["是否存续"] == 2 )]
fund_info_zuhe = fund_info_zuhe[["朝阳永续代码","私募机构","核心人物","最新规模","产品名称","成立日期","大类策略","细分策略1","细分策略2","是否存续","是否自营"]]
fund_info_zuhe["朝阳永续代码"] = fund_info_zuhe[["朝阳永续代码"]].astype(str)
fund_info_zuhe.set_index("朝阳永续代码",inplace = True)

# 恒天存续产品数据
#fund_info_cunxu = fund_info[(fund_info["是否存续"] == 1)]
#fund_info_cunxu = fund_info_cunxu[["恒天编码","私募机构","核心人物","最新规模","产品名称","成立日期","大类策略","细分策略1","细分策略2","是否存续"]]
#fund_info_cunxu["恒天编码"] = fund_info_cunxu[["恒天编码"]].astype(str)
#fund_info_cunxu.set_index("恒天编码",inplace = True)

# 重点关注与国盛存续产品数据合并
fund_info_core = pd.concat([fund_info_guanzhu,fund_info_cunxu,fund_info_zuhe],axis=0)


# In[5]:


# 关注产品代码
fund_ID_guanzhu =fund_info_guanzhu.index.tolist()
# 存续产品列表
fund_ID_cunxu =fund_info_cunxu.index.tolist()
#组合产品代码
fund_info_zuhe =fund_info_zuhe.index.tolist()
#fund_ID_cunxu
# 基金代码合并：核心和存续和组合
fund_ID = fund_ID_guanzhu+fund_ID_cunxu+fund_info_zuhe
#fund_ID = fund_ID_guanzhu

# # 数据提取

# In[6]:

'''
# 数据库数据提取

import pymysql.cursors
import os
# 数据提取

# 1.打开数据库连接
   
config = {
        'host': '106.75.45.237',
        'port': 15777,
        'user': 'simu_shcm',
        'password': '0WDNbK76YxacSRBk',
        'db': 'CUS_FUND_DB',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor,
        }


#print('连接服务器成功')
# 2.使用cursor()方法获取操作游标
#cursor = connect.cursor()
conn = pymysql.connect(**config)
cursor = conn.cursor()

# 使用execute方法执行SQL语句

#mysql> GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP ON systest.* TO root@'%' identified by 'root';
#Query OK, 0 rows affected (0.01 sec)
#sql_select_fund_nav = "SELECT * FROM CUS_FUND_DB.v2_adjusted_performance where fund_id in"+ str(tuple(fund_ID_guanzhu))
sql_select_fund_nav = "SELECT * FROM CUS_FUND_DB.v2_fund_nv_data_zyyx where fund_id in"+ str(tuple(fund_ID_guanzhu))
cursor.execute(sql_select_fund_nav)


# 使用 fetchone() 方法获取一条数据
results_fund_nav = cursor.fetchall()

print(results_fund_nav)
# 获取列名
col_name_list_fund_nav = [tuple[0] for tuple in cursor.description]
# 将数据转换成DataFrame格式
fund_nav_info = pd.DataFrame(list(results_fund_nav),columns=col_name_list_fund_nav)[["fund_id","fund_name","statistic_date","nav","swanav"]]
# 修改ID和日期格式为str
fund_nav_info[["fund_id"]]= fund_nav_info[["fund_id"]].astype("str")
# 重置索引为fund_id
fund_nav_info.columns = ["基金ID","基金简称","净值日期","单位净值","复权净值"]
# 关闭数据库连接
conn.close()
'''

# In[7]:


# 存续产品净值补充与合并
fund_nav_info_supplement = pd.read_excel(r'C:\Users\zhc12\Desktop\基金评价\周报\周报数据\存续净值全.xlsx')
#fund_nav_info_supplement = fund_nav_info_supplement[["产品编号","产品名称","净值日期","净值(元)","累计净值(元)"]]
fund_nav_info_supplement.columns = ["基金ID","基金简称","净值日期","单位净值","复权净值"]
#fund_nav_info_supplement = fund_nav_info_supplement[(fund_nav_info_supplement["基金ID"].isin(fund_ID_cunxu))]
#fund_nav_info_supplement["净值日期"] = fund_nav_info_supplement[["净值日期"]].astype("datetime64")
fund_nav_info_supplement["净值日期"] = fund_nav_info_supplement[["净值日期"]].astype("datetime64[ns]")
fund_nav_info_supplement[["基金ID"]]= fund_nav_info_supplement[["基金ID"]].astype("str")
fund_nav_info_supplement.sort_values("净值日期",ascending =False)
# 跟踪产品净值
fund_nav_info_supplement1 = pd.read_excel(r'C:\Users\thinker\Desktop\公募研究\国盛\Python代码基金分析\跟踪池数据最新.xlsx')
#fund_nav_info_supplement1.columns = ["null","基金ID","基金简称","净值日期","复权净值"]
fund_nav_info_supplement1.columns = ["基金ID","基金简称","净值日期","单位净值","复权净值"]
fund_nav_info_supplement1[["基金ID"]]= fund_nav_info_supplement1[["基金ID"]].astype("str")
#del fund_nav_info_supplement1["null"]

#组合产品净值
fund_nav_info_supplement2 = pd.read_excel(r'C:\Users\thinker\Desktop\公募研究\国盛\Python代码基金分析\组合投资.xlsx')
fund_nav_info_supplement2.columns = ["基金ID","基金简称","净值日期","单位净值","复权净值"]
fund_nav_info_supplement2[["基金ID"]]= fund_nav_info_supplement2[["基金ID"]].astype("str")


# 净值合并
fund_nav_info = pd.concat([fund_nav_info_supplement2,fund_nav_info_supplement1,fund_nav_info_supplement],axis=0)
fund_nav_info = fund_nav_info.sort_values("净值日期",ascending =True)
#fund_nav_info = fund_nav_info_supplement1.sort_values("净值日期",ascending =True)

# In[8]:


fund_nav_info


# In[9]:


fund_nav_info.to_excel(r'C:\Users\thinker\Desktop\公募研究\国盛\Python代码基金分析\基金净值数据1.xlsx')


# # 计算最新净值日期

# In[10]:


# 计算各基金各区间业绩
fund_return_all_period =fund_info_core
#fund_return_all_period =fund_info_guanzhu
# 最新净值日期
fund_latest_date = []
for code in fund_ID:
#     print(code)
    if len(fund_nav_info[fund_nav_info["基金ID"] == code]["净值日期"].values) == 0:
        fund_latest_date.append("")
    else:
        fund_latest_date.append(fund_nav_info[fund_nav_info["基金ID"] == code]["净值日期"].values.max())
fund_return_all_period["最新净值日期"] = fund_latest_date


# # 计算区间业绩

# In[11]:


# 定义基金收益率函；参数为：开始日期，截至日期，基金净值（索引为时间，净值为列名为“复权净值”）
def fund_return(start_date,end_date,fund_nav):
    fund_nav.sort_index(ascending = 1)    
    if start_date<fund_nav.index[0] or end_date >fund_nav.index[-1]:
        fund_return = ""
    
    else:
        start_date_fund_nav = fund_nav[(fund_nav.index <=start_date)]["复权净值"][-1]
        end_date_fund_nav = fund_nav[(fund_nav.index <=end_date)]["复权净值"][-1]
        fund_return =float(end_date_fund_nav/start_date_fund_nav-1)
    return fund_return


# In[12]:


#业绩计算    
for fund_start_date,fund_end_date,fund_return_columns in zip(return_start_date_list, return_end_date_list,return_start_end_date.index.tolist()):
    fund_return_tem = []
#     print(fund_start_date)
    
    for fund_code in fund_ID:
#         print(fund_code)
        one_fund_nav = fund_nav_info[(fund_nav_info["基金ID"] == fund_code)]
        one_fund_nav.set_index("净值日期",inplace = True)

        if len(one_fund_nav.index)<=5:
            fund_return_tem.append("")
        else:
            fund_return_tem.append(fund_return(fund_start_date,fund_end_date,one_fund_nav))
    fund_return_all_period[fund_return_columns] = fund_return_tem




# # 最大回撤

# In[14]:


# 定义最大回撤公式  MaxDrawdown_all(fund_nav)
def MaxDrawdown(return_list):
    '''最大回撤率'''
    i = np.argmax((np.maximum.accumulate(return_list) - return_list) / np.maximum.accumulate(return_list))  # 结束位置
    if i == 0:
        return 0
    j = np.argmax(return_list[:i])  # 开始位置
    return -(return_list[j] - return_list[i]) / (return_list[j])
def MaxDrawdown_all(fund_nav):
    MaxDrawdown_all = []
    for name in fund_nav.columns.tolist():
        MaxDrawdown_all.append(MaxDrawdown(fund_nav[name]))
    MaxDrawdown_all_2= pd.DataFrame(MaxDrawdown_all,index = fund_nav.columns,columns = ["最大回撤"]).T
    return MaxDrawdown_all_2


# In[15]:


# 计算最大回撤
for fund_start_date,fund_end_date,fund_MaxDrawdown_columns in zip(MaxDrawdown_start_date_list, MaxDrawdown_end_date_list,MaxDrawdown_start_end_date.index.tolist()):
    fund_MaxDrawdown_tem = []
    for fund_code in fund_ID:

        one_fund_nav = fund_nav_info[(fund_nav_info["基金ID"] == fund_code)&(fund_nav_info["净值日期"] >=fund_start_date)&(fund_nav_info["净值日期"] <=fund_end_date)]
        one_fund_nav.set_index("净值日期",inplace = True)

        if len(one_fund_nav.index) <=5:
            MaxDrawdown_all_value = ""
        else:
            MaxDrawdown_all_value = float(MaxDrawdown_all(one_fund_nav[["复权净值"]]).values)
        fund_MaxDrawdown_tem.append(MaxDrawdown_all_value)
    fund_return_all_period[fund_MaxDrawdown_columns] = fund_MaxDrawdown_tem




# # 产品各区间业绩起始日期

# In[18]:

# 年化收益 平均年化收益率法
def Annual_Return_m(fund_nav,period):    #period  --交易日度：250；周度：50；月度：12
    fund_return_day = (fund_nav/fund_nav.shift(1)-1).dropna()  #每日收益率
    Annual_Return_m = (1+fund_return_day.mean(axis= 0))**period-1
    return Annual_Return_m

# 计算年化收益 平均法
for fund_start_date,fund_end_date,fund_Annual_Return_m_columns in zip(Annual_Return_m_start_date_list, Annual_Return_m_end_date_list,Annual_Return_m_start_end_date.index.tolist()):
    fund_Annual_Return_m_tem = []
    for fund_code in fund_ID:

        one_fund_nav = fund_nav_info[(fund_nav_info["基金ID"] == fund_code)&(fund_nav_info["净值日期"] >=fund_start_date)&(fund_nav_info["净值日期"] <=fund_end_date)]
        one_fund_nav.set_index("净值日期",inplace = True)

        if len(one_fund_nav.index) <= 5:
            Annual_Return_m_value = ""
        else:
            Annual_Return_m_value = float(Annual_Return_m(one_fund_nav[["复权净值"]],50))
        fund_Annual_Return_m_tem.append(Annual_Return_m_value)
    fund_return_all_period[fund_Annual_Return_m_columns] = fund_Annual_Return_m_tem

# 年化收益 区间年化收益法 定义基金收益率函；参数为：开始日期，截至日期，基金净值（索引为时间，净值为列名为“复权净值”）
# 统计周期 单位：周W
def week_between(start_date,end_date):
    weeks = rrule.rrule(rrule.WEEKLY, dtstart = start_date, until = end_date)
    return weeks.count()
 

def Annual_Return_i(start_date,end_date,fund_nav):
    fund_nav.sort_index(ascending = 1)    
    if start_date<fund_nav.index[0] or end_date >fund_nav.index[-1]:
        Annual_Return_i = ""
    
    else:
        start_date_fund_nav = fund_nav[(fund_nav.index <=start_date)]["复权净值"][-1]
        end_date_fund_nav = fund_nav[(fund_nav.index <=end_date)]["复权净值"][-1]
        W = week_between(start_date,end_date)
        Annual_Return_i =float(end_date_fund_nav/start_date_fund_nav)**(50/W)-1
    return Annual_Return_i

# 计算年化收益 区间法
#业绩计算    
for fund_start_date,fund_end_date,fund_Annual_Return_i_columns in zip(Annual_Return_i_start_date_list, Annual_Return_i_end_date_list,Annual_Return_i_start_end_date.index.tolist()):
    fund_Annual_Return_i_tem = []
#     print(fund_start_date)
    
    for fund_code in fund_ID:
#         print(fund_code)
        one_fund_nav = fund_nav_info[(fund_nav_info["基金ID"] == fund_code)]
        one_fund_nav.set_index("净值日期",inplace = True)

        if len(one_fund_nav.index)<=5:
            fund_Annual_Return_i_tem.append("")
        else:
            fund_Annual_Return_i_tem.append(Annual_Return_i(fund_start_date,fund_end_date,one_fund_nav))
    fund_return_all_period[fund_Annual_Return_i_columns] = fund_Annual_Return_i_tem


# 年化波动
def Annual_Volatility(fund_nav,period):    #period  --交易日度：250；周度：50；月度：12
    fund_return_day = (fund_nav/fund_nav.shift(1)-1).dropna()  #每日收益率
    Annual_Volatility = float(fund_return_day.values.std())*50**0.5
    return Annual_Volatility

# 计算年化波动
for fund_start_date,fund_end_date,fund_Annual_Volatility_columns in zip(Annual_Volatility_start_date_list, Annual_Volatility_end_date_list,Annual_Volatility_start_end_date.index.tolist()):
    fund_Annual_Volatility_tem = []
    for fund_code in fund_ID:

        one_fund_nav = fund_nav_info[(fund_nav_info["基金ID"] == fund_code)&(fund_nav_info["净值日期"] >=fund_start_date)&(fund_nav_info["净值日期"] <=fund_end_date)]
        one_fund_nav.set_index("净值日期",inplace = True)

        if len(one_fund_nav.index) <= 5:
            Annual_Volatility_value = ""
        else:
            Annual_Volatility_value = float(Annual_Volatility(one_fund_nav[["复权净值"]],50))
        fund_Annual_Volatility_tem.append(Annual_Volatility_value)
    fund_return_all_period[fund_Annual_Volatility_columns] = fund_Annual_Volatility_tem
    
# # 夏普比率
# 夏普比率 平均年化收益法
def Sharpe(fund_nav,period):    #period  --交易日度：250；周度：50；月度：12
    rf =(1+0.015)**(1/period)-1  #无风险收益率，按周计算
    fund_return_day = (fund_nav/fund_nav.shift(1)-1).dropna()  #每日收益率
    return_yearly = (1+fund_return_day.mean(axis= 0))**period-1 #由于部分产品净值包含日度，平均年化收益不准
    stdev_yearly = float(fund_return_day.values.std())*50**0.5
    Sharpe = (return_yearly -rf)/stdev_yearly
    return Sharpe


# In[17]:

# 计算Sharpe 平均年化收益法
for fund_start_date,fund_end_date,fund_Sharpe_columns in zip(Sharpe_start_date_list, Sharpe_end_date_list,Sharpe_start_end_date.index.tolist()):
    fund_Sharpe_tem = []
    for fund_code in fund_ID:

        one_fund_nav = fund_nav_info[(fund_nav_info["基金ID"] == fund_code)&(fund_nav_info["净值日期"] >=fund_start_date)&(fund_nav_info["净值日期"] <=fund_end_date)]
        one_fund_nav.set_index("净值日期",inplace = True)

        if len(one_fund_nav.index) <= 5:
            Sharpe_value = ""
        else:
            Sharpe_value = float(Sharpe(one_fund_nav[["复权净值"]],50))
        fund_Sharpe_tem.append(Sharpe_value)
    fund_return_all_period[fund_Sharpe_columns] = fund_Sharpe_tem
# In[16]:
'''
def Sharpe_i(start_date,end_date,fund_nav):
    fund_nav.sort_index(ascending = 1)    
    if start_date<fund_nav.index[0] or end_date >fund_nav.index[-1]:
        Annual_Return_i = ""
    
    else:
        start_date_fund_nav = fund_nav[(fund_nav.index <=start_date)]["复权净值"][-1]
        end_date_fund_nav = fund_nav[(fund_nav.index <=end_date)]["复权净值"][-1]
        W = week_between(start_date,end_date)
        Annual_Return_i =float(end_date_fund_nav/start_date_fund_nav)**(50/W)-1
    rf = 0.015  #无风险收益率 一年定存利率
    fund_return_day = (fund_nav/fund_nav.shift(1)-1).dropna()  #每周收益率
    stdev_yearly = float(fund_return_day.values.std())*50**0.5  
    Sharpe_i = (Annual_Return_i -rf)/stdev_yearly
    return Sharpe_i

# 计算Sharpe 区间年化收益法
for fund_start_date,fund_end_date,fund_Sharpe_i_columns in zip(Sharpe_i_start_date_list, Sharpe_i_end_date_list,Sharpe_i_start_end_date.index.tolist()):
    fund_Sharpe_i_tem = []
    for fund_code in fund_ID:

        one_fund_nav = fund_nav_info[(fund_nav_info["基金ID"] == fund_code)]
        one_fund_nav.set_index("净值日期",inplace = True)

        if len(one_fund_nav.index) <= 5:
            fund_Sharpe_i_tem.append("")
        else:
            fund_Sharpe_i_tem.append(float(Sharpe_i(fund_start_date,fund_end_date,one_fund_nav)))
    fund_return_all_period[fund_Sharpe_i_columns] = fund_Sharpe_i_tem
'''


# 月度收益
def Mongthly_Return(start_date,end_date,fund_nav):
    fund_nav.sort_index(ascending = 1)    
    if start_date<fund_nav.index[0] or end_date >fund_nav.index[-1]:
        fund_return = ""
    
    else:
        start_date_fund_nav = fund_nav[(fund_nav.index <=start_date)]["复权净值"][-1]
        end_date_fund_nav = fund_nav[(fund_nav.index <=end_date)]["复权净值"][-1]
        fund_return =float(end_date_fund_nav/start_date_fund_nav-1)
    return fund_return

# 计算月度收益
for fund_start_date,fund_end_date,fund_return_columns in zip(Mongthly_Return_start_date_list, Mongthly_Return_end_date_list,Mongthly_Return_start_end_date.index.tolist()):
    fund_return_tem = []
#     print(fund_start_date)
    
    for fund_code in fund_ID:
#         print(fund_code)
        one_fund_nav = fund_nav_info[(fund_nav_info["基金ID"] == fund_code)]
        one_fund_nav.set_index("净值日期",inplace = True)

        if len(one_fund_nav.index)<=5:
            fund_return_tem.append("")
        else:
            fund_return_tem.append(fund_return(fund_start_date,fund_end_date,one_fund_nav))
    fund_return_all_period[fund_return_columns] = fund_return_tem
# 产品各区间业绩起始日期 
''''for fund_start_date,fund_end_date,fund_return_columns in zip(return_start_date_list, return_end_date_list,return_start_end_date.index.tolist()):
    fund_return_start_date_tem = []
    fund_return_end_date_tem = []
        
    for fund_code in fund_ID:

        one_fund_nav = fund_nav_info[(fund_nav_info["基金ID"] == fund_code)]
        one_fund_nav.set_index("净值日期",inplace = True)
        if len(one_fund_nav.index)<=2:
            fund_return_start_date = ""
            fund_return_end_date = ""
        elif fund_start_date<one_fund_nav.index[0] or fund_end_date > one_fund_nav.index[-1] :
            fund_return_start_date = ""
            fund_return_end_date = ""
        else:
            fund_return_start_date = one_fund_nav[(one_fund_nav.index <=fund_start_date)].index[-1]
            fund_return_start_date = datetime.datetime.strftime(fund_return_start_date,'%Y-%m-%d')
            fund_return_end_date = one_fund_nav[(one_fund_nav.index <=fund_end_date)].index[-1]
            fund_return_end_date = datetime.datetime.strftime(fund_return_end_date,'%Y-%m-%d')
        fund_return_start_date_tem.append(fund_return_start_date)
        fund_return_end_date_tem.append(fund_return_end_date)
    fund_return_all_period[fund_return_columns+"开始日期"] = fund_return_start_date_tem
    fund_return_all_period[fund_return_columns+"截止日期"] = fund_return_end_date_tem
fund_return_all_period.head()'''


# In[19]:


fund_nav_info.to_excel(r'C:\Users\thinker\Desktop\公募研究\国盛\Python代码基金分析\基金净值数据.xlsx')


# # 数据导出

# In[20]:


# 将成立日期和最新净值日期两列调整为str格式
fund_return_all_period["成立日期"] = fund_return_all_period[["成立日期"] ].astype(str)
fund_return_all_period["最新净值日期"] = fund_return_all_period[["最新净值日期"] ].astype(str)


# In[21]:


fund_strategy_list = fund_return_all_period["大类策略"].unique().tolist() #策略类型列表

#fund_return_all_period_ 与策略类型合并
fund_return_all_period_by_strategy = []
for name in fund_strategy_list:
    fund_return_all_period_by_strategy.append("fund_return_all_period_"+str(name))

# 各策略的业绩表现
for i in range(len(fund_return_all_period_by_strategy)):
    fund_return_all_period_by_strategy[i] = fund_return_all_period[(fund_return_all_period["大类策略"] == fund_strategy_list[i])]
#导出数据
with pd.ExcelWriter(r'C:\Users\thinker\Desktop\公募研究\国盛\Python代码基金分析\私募基金业绩表现'+datetime.datetime.strftime(end_date,'%Y-%m-%d')+".xlsx") as writer:
    fund_return_all_period.to_excel(writer, sheet_name="汇总")    
    for i in range(len(fund_return_all_period_by_strategy)):
        fund_return_all_period_by_strategy[i].to_excel(writer, sheet_name=fund_strategy_list[i])
    fund_return_all_period[(fund_return_all_period["是否存续"] == 1)].to_excel(writer, sheet_name="线上产品")
    fund_return_all_period[(fund_return_all_period["是否存续"] == 2)].to_excel(writer, sheet_name="FOF组合")
    fund_nav_info.to_excel(writer, sheet_name="基金净值数据")

# In[ ]:





# In[ ]:




