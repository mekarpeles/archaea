from waltz import render, web
from models.task import Project

class Create:
    def GET(self):
        projects = Project.getall()
        return render().addproject(projects)

    def POST(self):
        i = web.input(name='')
        p = Project(i.name)
        p.insert()
        raise web.seeother('/addproject')
