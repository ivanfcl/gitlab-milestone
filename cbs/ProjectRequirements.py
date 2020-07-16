import xlrd

def read_excel():
    ExcelFile = xlrd.open_workbook(r'需求条目_货债2.6.8.xls')
    req_sheet = ExcelFile.sheet_by_name('需求条目')

    req_info = []

    for i in range(0,req_sheet.nrows):
        systemname = req_sheet.cell(i,23).value
        if(systemname == '拍卖交易系统-同业存单实例（ICDIS）'):
            req_info.append(req_sheet.cell(i,0).value + '-' + req_sheet.cell(i,1).value)

    return req_info

if __name__ == '__main__':
    print(read_excel())