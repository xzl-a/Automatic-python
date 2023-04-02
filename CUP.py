from pyecharts.charts import Line
import pandas as pd
from pyecharts import options as opts
import random
#模拟数据，生成cpu使用率的折线图
x =list(pd.date_range('20220701','20220830'))
y=[random.randint(10,30) for i in range(len(x))]
z=[random.randint(5,20) for i in range(len(x))]
line = Line(init_opts = opts.InitOpts(width ='800px',height ='600px'))
line.add_xaxis(xaxis_data =x)
line.add_yaxis(series_name = 'cpu使用率',y_axis = y,is_smooth=True)
line.add_yaxis(series_name = '内存使用率',y_axis = z,is_smooth=True)
#添加参数，title_opts设置图的标题
line.set_global_opts(title_opts = opts.TitleOpts(title ='CPU和内存使用率折线图'))
line.render("/var/www/html/index.html")#生成一个render.html浏览器打开