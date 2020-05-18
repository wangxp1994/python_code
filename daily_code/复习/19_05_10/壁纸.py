import ctypes

path = "D:\\pythonWork\复习案例\\19_05_09\壁纸下载\\003311-1504369991759e.jpg"

ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)