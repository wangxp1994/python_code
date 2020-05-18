
import xlwt
import xlrd

namelst = ["吕布", "貂蝉", "刘备", "诸葛亮"]
filename = "demo.xls"

# 写入表格
def writeExcel():
    # 新建一个excel文件
    file = xlwt.Workbook()

    # 新建一个sheet
    table = file.add_sheet("sheet_name")

    # 设置表格列宽
    table.col(0).width = 256 * 5
    table.col(1).width = 256 * 20

    # 写入数据 table.write(行, 列, value, style)
    table.write(0, 0, "id")
    table.write(0, 1, "name")
    for n,v in enumerate(namelst):
        table.write(n+1, 0, n+1)
        table.write(n+1, 1, v)

    # 保存文件
    file.save(filename)

# 读取表格
"""
0 empty（空的）
1 string（text）
2 number 
3 date 
4 boolean 
5 error 
6 blank（空白表格）
"""
def readExcel():
    # 打开Excel文件
    data = xlrd.open_workbook(filename)

    # 返回所有工作表名字
    print(data.sheet_names())

    # 获取其中一个工作表
    # table = data.sheets()[0] #通过索引获取
    # table = data.sheet_by_index(0) #通过索引获取
    table = data.sheet_by_name("sheet_name")

    # 获取sheet中有效行数
    nrows = table.nrows
    print(nrows)

    for rowx in range(nrows):
        # table.row_xxx(rowx, start, end)
        # print table.row_slice(rowx) #返回该行中所有的单元格对象组成的列表
        # print table.row_types(rowx) #返回由该行中所有单元格的数据类型组成的列表
        print(table.row_values(rowx)) #返回由该行中所有单元格的数据组成的列表

    # 列的操作
    ncols = table.ncols
    print(ncols)
    print(table.col_slice(0))
    print(table.col_types(0))
    print(table.col_values(0))

    # 单元格操作
    one = table.cell(1, 1)
    print(one, one.ctype, one.value)


if __name__ == "__main__":
    # writeExcel()
    # print u"表格已保存"

    readExcel()

