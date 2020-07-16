import os
import sys
import os.path
import urllib
import datetime
import time
from termcolor import *
import GitProjectInfo as git
import requests
import json
def main():
    gl = git.GitLabAPI()
    projectname = 'isu/NCDS'
    project = gl.get_project_by_projectname(projectname)
    milestone = project.milestones.list()
    for i in milestone:
        totalTitle = "| 需求条目 | 未分配 | 需求阶段 | 设计阶段 | 开发阶段 | ST阶段 | UAT1阶段 | UAT2阶段 | 模拟 | "
        totalTitle += "\n" + "| ---- | " + "---- | " + "---- | " + "---- | " + "---- | " + "---- | " + "---- | " + "---- | "+ "---- | "
        #url = 'http://gitlab/api/v4/projects/3354/milestones/'+ str(i.id) +'?private_token=ejXsCbQkxcrYRDE7xKKd'
        issues = gl.get_issues_from_milestone(projectname, i.title)
        for j in issues:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d')
            due_time = str(j.due_date)
            totalTitle += "\n" + "| " + "<a href=" + j.web_url + ">" + j.title + "</a> |"
            assigner = "未分配"
            if (len(j.assignees) != 0):
                assigner = j.assignees[0]['name']
            # for k in j.assignees:
            #     print(k['name'])
            if j.labels == []:
                due_date = str(j.due_date)
                if now_time.__le__(due_time):
                    totalTitle += "  进行中 <br/> 人员: </br>" + assigner + "<br/> </br>" + "截止日期:" + due_date + " | "
                else:
                    totalTitle += " 进行中 <br/>  人员: </br>" + assigner + "<br/> </br>" + "`截止日期:" + due_date + "` | "
            else:
                totalTitle += "   | "  # 未分配

            if ("需求阶段" in j.labels):
                due_date = str(j.due_date)
                if now_time.__le__(due_time):
                    totalTitle += "  进行中 <br/> 人员: </br>" + assigner + "<br/> </br>" + "截止日期:" + due_date + " | "
                else:
                    totalTitle += " 进行中 <br/>  人员: </br>" + assigner + "<br/> </br>" + "`截止日期:" + due_date + "` | "
            else:
                totalTitle += "   | "  # 需求阶段
            if ("设计阶段" in j.labels):
                due_date = str(j.due_date)
                if now_time.__le__(due_time):
                    totalTitle += "  进行中 <br/> 人员: </br>" + assigner + "<br/> </br>" + "截止日期:" + due_date + " | "
                else:
                    totalTitle += " 进行中 <br/>  人员: </br>" + assigner + "<br/> </br>" + "`截止日期:" + due_date + "` | "
            else:
                totalTitle += "   | "  # 设计阶段
            if ("开发阶段" in j.labels):
                due_date = str(j.due_date)
                if now_time.__le__(due_time):
                    totalTitle += "  进行中 <br/> 人员: </br>" + assigner + "<br/> </br>" + "截止日期:" + due_date + " | "
                else:
                    totalTitle += " 进行中 <br/>  人员: </br>" + assigner + "<br/> </br>" + "`截止日期:" + due_date + "` | "
            else:
                totalTitle += "   | "  # 开发阶段
            if ("ST阶段" in j.labels):
                due_date = str(j.due_date)
                if now_time.__le__(due_time):
                    totalTitle += "  进行中 <br/> 人员: </br>" + assigner + "<br/> </br>" + "截止日期:" + due_date + " | "
                else:
                    totalTitle += " 进行中 <br/>  人员: </br>" + assigner + "<br/> </br>" + "`截止日期:" + due_date + "` | "
            else:
                totalTitle += "   | "  # ST阶段
            if ("UAT1阶段" in j.labels):
                due_date = str(j.due_date)
                if now_time.__le__(due_time):
                    totalTitle += "  进行中 <br/> 人员: </br>" + assigner + "<br/> </br>" + "截止日期:" + due_date + " | "
                else:
                    totalTitle += " 进行中 <br/>  人员: </br>" + assigner + "<br/> </br>" + "`截止日期:" + due_date + "` | "
            else:
                totalTitle += "   | "  # UAT1阶段
            if ("UAT2阶段" in j.labels):
                due_date = str(j.due_date)
                if now_time.__le__(due_time):
                    totalTitle += "  进行中 <br/> 人员: </br>" + assigner + "<br/> </br>" + "截止日期:" + due_date + " | "
                else:
                    totalTitle += " 进行中 <br/>  人员: </br>" + assigner + "<br/> </br>" + "`截止日期:" + due_date + "` | "
            else:
                totalTitle += "   | "  # UAT2阶段
            if ("模拟" in j.labels):
                due_date = str(j.due_date)
                if now_time.__le__(due_time):
                    totalTitle += "  进行中 <br/> 人员: </br>" + assigner + "<br/> </br>" + "截止日期:" + due_date + " | "
                else:
                    totalTitle += " 进行中 <br/>  人员: </br>" + assigner + "<br/> </br>" + "`截止日期:" + due_date + "` | "
            else:
                totalTitle += "   | "  # 模拟
                # l = requests.put(url + '&' + 'description=' + totalTitle)
                # print(l.content)
        i.description = totalTitle
        i.save()
        #     if j.labels == []:
        #         due_date = str(j.due_date)
        #         if now_time.__le__(due_time):
        #             totalTitle += "  进行中  <br/> </br>" + "截止日期:" + due_date + " | "
        #         else:
        #             totalTitle += " `进行中 ` <br/> </br>" + "`截止日期:" + due_date + "` | "
        #     else:
        #         totalTitle += "   | "  # 未分配
        #
        #     if ("需求阶段" in j.labels):
        #         due_date = str(j.due_date)
        #         if now_time.__le__(due_time):
        #             totalTitle += "  进行中 <br/> </br>" + "截止日期:" + due_date + " | "
        #         else:
        #             totalTitle += " `进行中 ` <br/> </br>" + "`截止日期:" + due_date + "` | "
        #     else:
        #         totalTitle += "   | "  # 需求阶段
        #     if ("设计阶段" in j.labels):
        #         due_date = str(j.due_date)
        #         if now_time.__le__(due_time):
        #             totalTitle += "  进行中  <br/> </br>" + "截止日期:" + due_date + " | "
        #         else:
        #             totalTitle += " `进行中 ` <br/> </br>" + "`截止日期:" + due_date + "` | "
        #     else:
        #         totalTitle += "   | "  # 设计阶段
        #     if ("开发阶段" in j.labels):
        #         due_date = str(j.due_date)
        #         if now_time.__le__(due_time):
        #             totalTitle += "  进行中  <br/> </br>" + "截止日期:" + due_date + " | "
        #         else:
        #             totalTitle += " `进行中 ` <br/> </br>" + "`截止日期:" + due_date + "` | "
        #     else:
        #         totalTitle += "   | "  # 开发阶段
        #     if ("ST阶段" in j.labels ):
        #         due_date = str(j.due_date)
        #         if now_time.__le__(due_time):
        #             totalTitle += "  进行中  <br/> </br>" + "截止日期:" + due_date + " | "
        #         else:
        #             totalTitle += " `进行中 ` <br/> </br>" + "`截止日期:" + due_date + "` | "
        #     else:
        #         totalTitle += "   | "  # ST阶段
        #     if ("UAT1阶段" in j.labels):
        #         due_date = str(j.due_date)
        #         if now_time.__le__(due_time):
        #             totalTitle += "  进行中  <br/> </br>" + "截止日期:" + due_date + " | "
        #         else:
        #             totalTitle += " `进行中 ` <br/> </br>" + "`截止日期:" + due_date + "` | "
        #     else:
        #         totalTitle += "   | "  # UAT1阶段
        #     if ("UAT2阶段" in j.labels):
        #         due_date = str(j.due_date)
        #         if now_time.__le__(due_time):
        #             totalTitle += "  进行中  <br/> </br>" + "截止日期:" + due_date + " | "
        #         else:
        #             totalTitle += " `进行中 ` <br/> </br>" + "`截止日期:" + due_date + "` | "
        #     else:
        #         totalTitle += "   | "  # UAT2阶段
        #     if ("模拟" in j.labels):
        #         due_date = str(j.due_date)
        #         if now_time.__le__(due_time):
        #             totalTitle += "  进行中  <br/> </br>" + "截止日期:" + due_date + " | "
        #         else:
        #             totalTitle += " `进行中 ` <br/> </br>" + "`截止日期:" + due_date + "` | "
        #     else:
        #         totalTitle += "   | "  # 模拟
        # # l = requests.put(url + '&' + 'description=' + totalTitle)
        # # print(l.content)
        # i.description = totalTitle
        # i.save()
if __name__ == '__main__':
        main()

