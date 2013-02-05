from waltz import render
from models.task import User, Task, Project, PRIORITIES, STATUSES

class Index:
    def GET(self):
        tasks = Task.getall()
        users = User.getall()
        projects = Project.getall()
        return render().index(tasks, users, projects,
                            priorities=PRIORITIES, statuses=STATUSES)

