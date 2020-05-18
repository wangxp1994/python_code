import sys, os
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton
from PyQt5.QtGui import QPalette,QBrush,QPixmap
import ctypes

css1 = '''font-size:16px;
    color:red;
    text-align:center;
    font-family:"Microsoft YaHei"'''

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

        self.n = 0
        self.path = "D:\\pythonWork\复习案例\\19_05_09\壁纸下载\\"
        self.imgList = os.listdir(self.path)
        self.bz()
                
        self.setFixedSize(self.width(),self.height())

    def initUI(self):
        self.setGeometry(300,300,1200,650)
        self.setWindowTitle("壁纸")        

        b1 = QPushButton("下一张",self)
        b1.setStyleSheet(css1)
        b1.move(10,60)
        b1.clicked.connect(self.clicked1)   

        b2 = QPushButton("上一张",self)
        b2.setStyleSheet(css1)
        b2.move(10,10)
        b2.clicked.connect(self.clicked2)  

        b3 = QPushButton("设置为壁纸",self)
        b3.setStyleSheet(css1)
        b3.move(120,10)
        b3.clicked.connect(self.clicked3) 

        self.show()

    def bz(self):
        palette1 = QPalette()
        pix = QPixmap(self.path + self.imgList[self.n])
        pix = pix.scaled(self.width(),self.height())
        palette1.setBrush(self.backgroundRole(),QBrush(pix))
        self.setPalette(palette1)

    def clicked1(self,event): 
        self.n += 1
        if self.n >= len(self.imgList):
            self.n = 0
        self.bz()       

    def clicked2(self,event): 
        self.n -= 1
        if self.n == 0:
            self.n = len(self.imgList) - 1
        self.bz()

    def clicked3(self,event):
        path = self.path + self.imgList[self.n]
        ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)

       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())