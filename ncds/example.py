import GitProjectInfo as git
import xlrd

def main():
    # ExcelFile = xlrd.open_workbook(r'需求条目_货债2.6.8.xls')
    # req_sheet = ExcelFile.sheet_by_name('需求条目')
    gl = git.GitLabAPI()
    projectname = 'isu/fxmss'
    project = gl.get_project_by_projectname(projectname)
    milestone = project.milestones.list()
    # mrs = gl.merge.requests.list()
    # for i in mrs:
    #     print(i)
    mrs = project.mergerequests.list(state='all')
    for i in mrs:
        print(i)











if __name__ == '__main__':
    main()

