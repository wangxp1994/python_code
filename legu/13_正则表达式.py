
import re

# 邮箱
html1 = """
   <h2>  荣誉、奖励及参加学术团体的情况：</h2>
     kground-color: rgb(255, 255, 255); font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px;">2015- 至今 中国细胞生物学学会理事长</span><br style="color: rgb(68, 68, 68); text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Arial, Helvetica, 微软雅黑, &quot;Microsoft YaHei&quot;, PingHei, STHeiti; font-size: 16px; font-style: normal; font-weight: normal; word-spacing: 0px; white-space: normal; orphans: 2; widows: 2; background-color: rgb(255, 255, 255); font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px;"/><span style="color: rgb(68, 68, 68); text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Arial, Helvetica, 微软雅黑, &quot;Microsoft YaHei&quot;, PingHei, STHeiti; font-size: 16px; font-style: normal; font-weight: normal; word-spacing: 0px; float: none; display: inline !important; white-space: normal; orphans: 2; widows: 2; background-color: rgb(255, 255, 255); font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px;">2011年&ldquo;中国细胞生物学学会－CST杰出成就奖&rdquo;</span><br style="color: rgb(68, 68, 68); text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Arial, Helvetica, 微软雅黑, &quot;Microsoft YaHei&quot;, PingHei, STHeiti; font-size: 16px; font-style: normal; font-weight: normal; word-spacing: 0px; white-space: normal; orphans: 2; widows: 2; background-color: rgb(255, 255, 255); font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px;"/><span style="color: rgb(68, 68, 68); text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Arial, Helvetica, 微软雅黑, &quot;Microsoft YaHei&quot;, PingHei, STHeiti; font-size: 16px; font-style: normal; font-weight: normal; word-spacing: 0px; float: none; display: inline !important; white-space: normal; orphans: 2; widows: 2; background-color: rgb(255, 255, 255); font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px;">2008年何梁何利科学与技术进步奖</span><br style="color: rgb(68, 68, 68); text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Arial, Helvetica, 微软雅黑, &quot;Microsoft YaHei&quot;, PingHei, STHeiti; font-size: 16px; font-style: normal; font-weight: normal; word-spacing: 0px; white-space: normal; orphans: 2; widows: 2; background-color: rgb(255, 255, 255); font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px;"/><span style="color: rgb(68, 68, 68); text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Arial, Helvetica, 微软雅黑, &quot;Microsoft YaHei&quot;, PingHei, STHeiti; font-size: 16px; font-style: normal; font-weight: normal; word-spacing: 0px; float: none; display: inline !important; white-space: normal; orphans: 2; widows: 2; background-color: rgb(255, 255, 255); font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px;">2007年&ldquo;新世纪百千万人才工程&rdquo;</span><br style="color: rgb(68, 68, 68); text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Arial, Helvetica, 微软雅黑, &quot;Microsoft YaHei&quot;, PingHei, STHeiti; font-size: 16px; font-style: normal; font-weight: normal; word-spacing: 0px; white-space: normal; orphans: 2; widows: 2; background-color: rgb(255, 255, 255); font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px;"/><span style="color: rgb(68, 68, 68); text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Arial, Helvetica, 微软雅黑, &quot;Microsoft YaHei&quot;, PingHei, STHeiti; font-size: 16px; font-style: normal; font-weight: normal; word-spacing: 0px; float: none; display: inline !important; white-space: normal; orphans: 2; widows: 2; background-color: rgb(255, 255, 255); font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px;">2006年中国青年科技奖</span><br style="color: rgb(68, 68, 68); text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Arial, Helvetica, 微软雅黑, &quot;Microsoft YaHei&quot;, PingHei, STHeiti; font-size: 16px; font-style: normal; font-weight: normal; word-spacing: 0px; white-space: normal; orphans: 2; widows: 2; background-color: rgb(255, 255, 255); font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px;"/><span style="color: rgb(68, 68, 68); text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Arial, Helvetica, 微软雅黑, &quot;Microsoft YaHei&quot;, PingHei, STHeiti; font-size: 16px; font-style: normal; font-weight: normal; word-spacing: 0px; float: none; display: inline !important; white-space: normal; orphans: 2; widows: 2; background-color: rgb(255, 255, 255); font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px;">2004年教育部&ldquo;中国高等学校十大科技进展&rdquo;</span><br style="color: rgb(68, 68, 68); text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Arial, Helvetica, 微软雅黑, &quot;Microsoft YaHei&quot;, PingHei, STHeiti; font-size: 16px; font-style: normal; font-weight: normal; word-spacing: 0px; white-space: normal; orphans: 2; widows: 2; background-color: rgb(255, 255, 255); font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px;"/><span style="color: rgb(68, 68, 68); text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Arial, Helvetica, 微软雅黑, &quot;Microsoft YaHei&quot;, PingHei, STHeiti; font-size: 16px; font-style: normal; font-weight: normal; word-spacing: 0px; float: none; display: inline !important; white-space: normal; orphans: 2; widows: 2; background-color: rgb(255, 255, 255); font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px;">2002-2003年度美国&ldquo;李氏基金杰出成就奖&rdquo;</span></p></p>
    
         <h2>  联系方式：</h2>
  <p><p>地址：北京市海淀区清华大学生命科学学院分子细胞实验室（100084）</p><p>电话：010-62784794</p><p>传真：010-62794376</p><p>E-mail：ygchen@mail.tsinghua.edu.cn</p><p>Websites: <a href="http://ygc.life.tsinghua.edu.cn/">http://ygc.life.tsinghua.edu.cn</a></p><p>&nbsp;</p></p>
        </div>
   </div>
  
  </div>
 </div>
"""
reg_str = r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+'
result = re.findall(reg_str, html1)
print(result)

html2 = """
<span style="font-family: 宋体; font-size: 16px;">邮件：chenyifang at cau.edu.cn</span>
"""
reg_str = r"([a-z0-9\.\-+_]+) at cau.edu.cn"
comp = re.compile(reg_str)
result = comp.findall(html2)
print(result)








