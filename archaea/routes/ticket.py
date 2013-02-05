from waltz import render, web
from models.task import User, Task, Project, PRIORITIES, STATUSES

class Create:
    def GET(self):
        users = User.getall()
        projects = Project.getall()
        return render().create(users=users, projects=projects,
                               priorities=PRIORITIES)

    def POST(self):
        i = web.input(title='', status_id=0, priority_id=0, desc='',
                      project_id=None, owner_id=None)
        task = Task(title=i.title, status_id=i.status_id, desc=i.desc,
                    priority_id=i.priority_id, project_id=i.project_id,
                    owner_id=i.owner_id)
        task.insert()
        raise web.seeother('/tasks')

class Delete:
    def GET(self):
        i = web.input(tid=None)
        if i.tid:
            try:
                Task.disable(i.tid)
            except:
                raise
        raise web.seeother('/tasks')

class Ticket:
    def GET(self, tid):
        try:
            task = Task.get(tid)
        except:
            raise web.seeother('/404')
        if not task:
            raise web.seeother('/404')
        users = User.getall()
        projects = Project.getall()
        return render().task(tid, task, users, projects, PRIORITIES,
                             STATUSES)

class Tickets:
    def GET(self):
        tasks = Task.getall()
        users = User.getall()
        projects = Project.getall()
        return render().tasks(tasks, users, projects,
                              priorities=PRIORITIES, statuses=STATUSES)
