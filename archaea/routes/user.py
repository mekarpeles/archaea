from waltz import render, web
from models.task import User, Task, Project, PRIORITIES, STATUSES

class Create:
    def GET(self):
        users = User.getall()
        return render().adduser(users)

    def POST(self):
        """TODO Import email validation lepl.rfc"""
        i = web.input(name='', username='', email='')
        u = User(i.name, i.username, i.email)
        u.insert()
        raise web.seeother('/adduser')
