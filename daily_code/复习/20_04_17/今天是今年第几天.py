import time

# 今天是今年第几天

# 返回某个月的天数
def monthDays(year, month):
    monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 闰年
    if year%400==0 or (year%100!=0 and year%4==0):
        monthList[1] += 1
    return monthList[month-1]

# 计算天数
def dayCount(year, month, day):
    year = int(year)
    month = int(month)
    count = int(day)
    for m in range(1, month):
        count += monthDays(year, m)
    return count

if __name__ == '__main__':
    count = dayCount(*time.strftime("%Y-%m-%d").split("-"))
    print(count)