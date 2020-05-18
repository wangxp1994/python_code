
from faker import Faker

# 设置语言
skt = Faker("zh_CN")
# skt = Faker()

print ("-"*20,u"地址相关","-"*20)
print (skt.country()) #阿拉伯联合酋长国
print (skt.city()) #凤兰市
print (skt.address()) #宁夏回族自治区俊县璧山济南街n座 383663
print (skt.street_address()) #南昌路B座
print (skt.street_name()) #长沙街
print (skt.postcode()) #484581 - 邮编

print ("-"*20,u"人物相关","-"*20)
print (skt.name()) #吴博
print (skt.last_name()) #谢
print (skt.first_name()) #志强
print (skt.name_male()) #赵柳
print (skt.name_female()) #罗琳

print ("-"*20,u"颜色相关","-"*20)
print (skt.hex_color()) # #f99417
print (skt.rgb_css_color()) #rgb(180,47,66)
print (skt.rgb_color()) #245,91,51
print (skt.color_name()) #WhiteSmoke

print ("-"*20,u"时间相关","-"*20)
print (skt.date_time()) #1988-03-20 22:22:19
print (skt.date_time_this_month()) #2019-05-27 06:36:44
print (skt.date_time_this_year()) #2019-03-03 19:52:36
print (skt.date_time_between(start_date="-5M", end_date="now")) #2019-03-08 05:38:34
print (skt.time()) #00:29:08
print (skt.month()) #06
print (skt.month_name()) #May
print (skt.year()) #1975
print (skt.day_of_week()) #Sunday
print (skt.day_of_month()) #28

print ("-"*20,u"文件相关","-"*20)
print (skt.file_name()) #专业.mov
print (skt.file_name(category="image")) #数据.bmp
print (skt.file_name(extension="txt")) #影响.txt
print (skt.file_extension()) #png

print ("-"*20,u"文字相关","-"*20)
print (skt.text())
print (skt.word())
print (skt.words(nb=3))
print (skt.sentence())

print ("-"*20,u"python相关","-"*20)
print (skt.pyint(0, 100)) #整数
print (skt.pyfloat()) #浮点数
print (skt.pystr()) #字符串
print (skt.pybool()) #布尔值
print (skt.pyiterable()) #迭代器
print (skt.pylist()) #列表
print (skt.pydict()) #字典
print (skt.pyset()) #集合
print (skt.pytuple()) #元组

print ("-"*20,u"其他","-"*20)
print (skt.job()) #房地产客服
print (skt.company()) #商软冠联传媒有限公司
print (skt.phone_number()) #15834043329
print (skt.safe_email()) #zhaomin@example.net
print (skt.free_email()) #pingyu@hotmail.com
print (skt.email()) #juan92@yahoo.com
print (skt.profile()) #生成人物描述信息
print (skt.ssn()) #身份证号码
print (skt.user_agent()) #伪造UA
print (skt.internet_explorer()) #IE浏览器
print (skt.chrome()) #谷歌浏览器