# code 自定义函数


# 获取表格中最大行数
def get_highest_row(sheet):
    # wb = openpyxl.load_workbook('example.xlsx')
    # sheet = wb['Sheet1']
    row_number = 0
    cell = sheet.cell(1, 1)
    print(cell.value)
    if not cell.value:
        return row_number
    else:
        row_number = 1
        row = 2
        while sheet.cell(row, 1).value:
            row_number = row_number + 1
            row = row + 1
    return row_number


# 获取表格中最大列数
def get_highest_col(sheet):
    # wb = openpyxl.load_workbook('example.xlsx')
    # sheet = wb['Sheet1']
    col_number = 0
    cell = sheet.cell(1, 1)
    print(cell.value)
    if not cell.value:
        return col_number
    else:
        col_number = 1
        col = 2
        while sheet.cell(1, col).value:
            col_number = col_number + 1
            col = col + 1
    return col_number