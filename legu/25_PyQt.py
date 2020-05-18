
import sys
import os
import zhconv
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ';' + os.environ['PATH']
from PyQt5.QtWidgets import QWidget,QApplication, QLabel, QVBoxLayout,\
        QLineEdit, QHBoxLayout, QPushButton


title_txt = "请把本程序放到要转换的文件目录"
input_txt = "请输入转换文件结尾(如json,js,csd),多种用空格隔开"
title_style = "color:green;"
input_style = "color:green;"
work_style = "color:red;background-color:rgba(135,206,255,0.5);"
yes_style = "background-color:pink;height:20px;border-radius:10px;border:1px solid red;"


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.path = os.path.dirname(__file__)
        self.save_path = self.path + "/OUT"
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("")
        self.initUI()

    def initUI(self):
        # 顶部文字
        self.lb_main = QLabel(title_txt)
        self.lb_main.setStyleSheet(title_style)
        # 显示框
        self.lb_work = QLabel()
        self.lb_work.setStyleSheet(work_style)
        # 输入框提示文字
        self.lb_input = QLabel(input_txt)
        self.lb_input.setStyleSheet(input_style)
        # 输入框
        self.input = QLineEdit()
        # 确定按钮
        self.lb_1 = QLabel()
        self.btn_yes = QPushButton("确定")
        self.btn_yes.setStyleSheet(yes_style)
        self.btn_yes.clicked.connect(self.exchange_event)

        self.layout_1 = QHBoxLayout()
        self.layout_1.addWidget(self.lb_1)
        self.layout_1.addWidget(self.btn_yes)


        self.layout=QVBoxLayout()
        self.layout.addWidget(self.lb_main)
        self.layout.addWidget(self.lb_work)
        self.layout.addWidget(self.lb_input)
        self.layout.addWidget(self.input)
        self.layout.addLayout(self.layout_1)


        self.setLayout(self.layout)
        self.show()

    def exchange_event(self, event):
        txt = self.input.text()
        self.type = txt.split(' ')
        self.lb_work.setText("开始工作")

        self.exchange_work(self.path, self.save_path)
        self.lb_work.setText("已完成")

    def exchange_work(self,from_dir, to_dir):
        if not os.path.exists(to_dir):
            os.makedirs(self.save_path)
            self.lb_work.setText("创建目录成功")
        # 获取目录文件
        dirlist = os.listdir(from_dir)
        for i in dirlist:
            if '.' not in i:
                continue
            elif i.split('.')[-1] not in self.type :
                continue
            else:
                from_path = from_dir + '/' + i
                to_path = to_dir + '/' + i
                with open(from_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    with open(to_path, 'w') as f1:
                        content = zhconv.convert(content, 'zh-tw')
                        f1.write(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

