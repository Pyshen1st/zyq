#python调用excel宏

import win32com.client
import os

for i in range(2):
    xls = win32com.client.Dispatch("Excel.Application")
    xls.Workbooks.Open(Filename = u"filename")
    xls.Application.Run("宏名称", 参数1, 参数2, ...)
    xls.Application.Quit()
    os.system('taskkill /F /IM EXCEL.EXE')     #通过任务管理器杀死excel，ppt进程
    os.system('taskkill /F /IM POWERPNT.EXE')

os.system('shutdown -s')   #程序执行结束以后关机
