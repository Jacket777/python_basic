# code02 : 从电子表格中读取数据

import openpyxl, pprint
import Tools as tools

def get_excel_data():
    print("Opening workbook....")
    wb = openpyxl.load_workbook('censuspopdata.xlsx')
    sheet = wb.get_sheet_by_name('Population by Census Tract')
    countyData = {}
    print("Reading row")
    for row in range(2, tools.get_highest_row(sheet)):
        print('-----------')
        state = sheet['B' + str(row)].value
        county = sheet['C' + str(row)].value
        pop = sheet['D' + str(row)].value
        # Make sure the key for this state exists
        countyData.setdefault(state, {})
        countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
        countyData[state][county]['tracts'] += 1
        countyData[state][county]['pop'] += int(pop)

    # 将结果存写入文件
    print('Writing result......')
    with open('censuspopdata.py', 'w') as f:
        f.write('allData = ' + pprint.pformat(countyData))
    print("Done..")


if __name__ == '__main__':
    get_excel_data()











if __name__ == '__main__':
    get_excel_data()
