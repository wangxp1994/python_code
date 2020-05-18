
"""
需要安装的模块 : zhconv
    pip install zhconv

将本程序放在需要转换的文件目录下,执行该程序,
会在该目录下创建子目录 OUT , 将转换的
文件放到该子目录下
"""

# 转换的文件类型
type_ = ["json", "js"]

import zhconv
import sys
import os

# 解决文件读写编码问题
reload(sys)
sys.setdefaultencoding('utf8')

class JsonTransform:

    def __init__(self):        
        self.path = os.path.dirname(__file__)
        self.savePath = self.path + "/OUT"

    # 创建保存目录
    def CreateDir(self):
        if not os.path.exists(self.savePath):
            os.makedirs(self.savePath)
            print("保存目录创建成功")

    # 读取目录下的所有type_文件
    def getJsonList(self): 

        path = self.path 
        lst = os.listdir(path)
        for i in lst:
            if self.fileType(i):
                fileFromPath = path + "/"+ i
                fileToPath = self.savePath + "/" + i   
                self.convertToZhtw(fileFromPath,fileToPath)
                print(i, "已保存")

    # 判断是否为type_文件
    def fileType(self,filename):
        if "." not in filename:
            return False       
        elif filename.split(".")[-1] in type_:
            return True
        else:
            return False

    # 将type_文件中简体转换为繁体
    def convertToZhtw(self, fileFromPath, fileToPath):
        with open(fileFromPath,'r') as f:
            content = f.read().decode("utf-8")       
            
            with open(fileToPath,'w') as f1:
                content = zhconv.convert(content, 'zh-tw')            
                f1.write(content)

    def run(self):
        self.CreateDir()
        self.getJsonList()

    
if __name__ == "__main__":
    jt = JsonTransform()
    jt.run() 
