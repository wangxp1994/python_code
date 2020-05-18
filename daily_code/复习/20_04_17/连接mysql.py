import faker
import pymysql
import random

skt = faker.Faker("zh_CN")

# 添加数据到mysql
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="wang",
    password="wxp520++",
    database="day17",
    charset="utf8"
)
cur = conn.cursor()

for i in range(50):
    name = skt.name()
    gender = random.choice("男女")
    age = random.randint(10,99)
    address = random.choice(["广西","广东","湖南"])
    qq = skt.phone_number()
    email = skt.email()
    sql = "insert into user(name,gender,age,address,qq,email) values('{}','{}','{}','{}','{}','{}');".format(
        name, gender, age, address, qq, email
    )
    print(sql)
    cur.execute(sql)
conn.commit()
cur.close()
conn.close()