# coding:utf-8
"""
python2.7
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

# 创建一个实例
driver = webdriver.Chrome()

# 一个例子
def one():
    # 打开网址
    driver.get("https://www.baidu.com/")

    # 找到输入节点
    """
        driver.find_element_by_id(),
        driver.find_element_by_name(),
        driver.find_element_by_xpath()    
    """
    input_ = driver.find_element_by_id("kw")

    # 清除文本
    input_.clear()

    # 输入校花
    input_.send_keys(u"校花")
    sleep(1)

    # 按下回车键
    input_.send_keys(Keys.ENTER)

    # 点击搜索按钮
    # search_ = driver.find_element_by_id("su")
    # search_.click()

# one()

 # 表单提交 --不是很明白--
def two():
    driver.get("http://i.360.cn/reg")

    # 选中表单节点
    form = driver.find_element_by_class_name("quc-form")

    select = Select(form)

    options = select.options

# two()

# 鼠标操作
def three():
    one()
    sleep(2)

    # 鼠标移到页面底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)

    # 操作的节点
    next = driver.find_element_by_xpath('//a[@class="n"]')

    act = ActionChains(driver)

    # 鼠标移动到节点
    # act.move_to_element(next).perform()

    # 鼠标右击节点
    # act.context_click(next).perform()

    # 鼠标双击节点
    # act.double_click(next).perform()

    # 鼠标拖动元素 drag_and_drop(source, target)
    # 鼠标悬停节点 move_to_element(element)
    # 鼠标单击节点 click(element)
    # 鼠标移动到坐标 move_by_offset(x, y)

sleep(2)
# 截图
# driver.get_screenshot_as_file("a.png")
driver.save_screenshot("a.png")
driver.close()