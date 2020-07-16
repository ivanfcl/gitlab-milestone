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
    projectname = 'isu/CDIS'
    project = gl.get_project_by_projectname(projectname)
    # ms = project.milestones.list()
    # print(type (ms))
    mras = project.approvals.get()
    for i in mras:
        print(i)

if __name__ == '__main__':
        main()

