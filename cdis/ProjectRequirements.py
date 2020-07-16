import xlrd

def read_excel():
    ExcelFile = xlrd.open_workbook(r'开发人员名字对照表.xlsx')
    req_sheet = ExcelFile.sheet_by_name('Sheet1')

    req_info = []

    for i in range(0,req_sheet.nrows):
        systemname = req_sheet.cell(i,1).value
        # if(systemname == '拍卖交易系统-同业存单实例（ICDIS）'):
        #     req_info.append(req_sheet.cell(i,0).value + '-' + req_sheet.cell(i,1).value)
        req_info.append(req_sheet.cell(i,0).value)
    del(req_info[0])
    print(req_info)
    #return req_info

if __name__ == '__main__':
    print(read_excel())