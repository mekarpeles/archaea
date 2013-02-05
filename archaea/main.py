#-*- coding: utf-8 -*-
"""
    main.py
    ~~~~~~~
    Archaaea lightweight scm bug tracker
    
    :copyright: (c) 2012 by Mek
    :license: BSD, see LICENSE for more details.
"""

import waltz
from waltz import web, render, session
from models.task import User, Task, Project, PRIORITIES, STATUSES
from configs.config import SERVER

urls = ('/', 'routes.index.Index',
        '/adduser/?', 'routes.user.Create',
        '/addproject/?', 'routes.project.Create',
        '/delete/?', 'routes.ticket.Delete',
        '/create/?', 'routes.ticket.Create',
        '/tasks/?', 'routes.ticket.Tickets',
        '/t([0-9]+)/?', 'routes.ticket.Ticket',
        '/404', 'NotFound',
        '(.*)', 'NotFound')

sessions = {"logged": False,
            "uid": None,
            "uname": "",
            }
app = waltz.setup.dancefloor(urls, globals(), sessions=sessions,
                             autoreload=False)

class NotFound:
    def GET(self, err=None):
        raise web.notfound("404")

if __name__ == "__main__":
    app.run()
