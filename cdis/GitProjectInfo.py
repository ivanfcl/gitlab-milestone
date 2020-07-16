import gitlab

import os
import sys
import ProjectRequirements as req

class GitLabAPI(object):
    def __init__(self, *args, **kwargs):
        self.gl = gitlab.Gitlab('http://gitlab', private_token='ejXsCbQkxcrYRDE7xKKd',per_page=2000)
        self.gl.auth()

    def get_all_projects(self):
        projects = self.gl.projects.list()
        return projects

    def get_project_by_projectname(self, projectname):
        project = self.gl.projects.get(projectname)
        return project

    def get_all_groups(self):
        groups = self.gl.groups.list()
        return groups

    def get_all_issues(self):
        issues = self.gl.issues.list()
        return issues



    def get_group_by_name(self, groupname):
        group = self.gl.groups.get(groupname)
        return group

    def get_issues_by_group(self, groupname):
        group = self.get_group_by_name(groupname)
        issues = group.issues.list()
        return issues

    def get_issues_by_project(self, projectname):
        project = self.get_project_by_projectname(projectname)
        issues = project.issues.list()
        return issues

    def get_boards_by_group(self, projectname):
        project = self.get_project_by_projectname(projectname)
        print(project)
        boards = project.boards.list()
        return boards

    def save_boards_req_issue_by_project(self, projectname,):
        project = self.get_project_by_projectname(projectname)
        requirements = req.read_excel()
        print(requirements)
        for r in requirements:
            print(r)
            issue = project.issues.create({'title': r})
            issue.labels = ['需求']
            issue.save()
            print(issue)

    def get_issues_from_milestone(self, projectname, version):
        project = self.get_project_by_projectname(projectname)
        milestones = project.milestones.list()
        for m in milestones:
            if (m.title == version):
                issues = m.issues()
        return issues

if __name__ == '__main__':

    git = GitLabAPI()
    groupname = 'isu'

    group = git.get_group_by_name(groupname)
    projectname = 'isu/CDIS'

    #issues = git.get_issues_from_milestone(projectname,'2.0.0')
    #for isu in issues:
    #    print(isu)
    # git.save_boards_req_issue_by_project(projectname)
    # project = git.get_project_by_projectname(projectname)
    # print(project)
    # milestones = project.milestones.list()
    # print(milestones)
    #
    # for m in milestones:
    #     issues = m.issues()
    #     print(issues)
