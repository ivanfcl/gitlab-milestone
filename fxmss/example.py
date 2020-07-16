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
    projectname = 'isu/fxmss'
    project = gl.get_project_by_projectname(projectname)
    # milestone = project.milestones.list()
    # issue = project.issues.list()
    # if (issue[15].labels == []):
    #     print("aaa")
    # else:
    #     print("bbb")
    ms = project.approvals.get()
    print(type(ms))

    # try:
    #     if (issue[0].labels == []):
    #         sys.exit(0)
    # except:
    #     sys.exit(1)

        # try:
        #     if (len(i.assignees) == 0) and i.labels == []:
        #         sys.exit(0)
        # except:
        #     sys.exit(1)



if __name__ == '__main__':
    main()

