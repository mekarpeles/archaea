#-*- coding: utf-8 -*-
"""
    task.py
    ~~~~~~~
    Models and APIs driving task, user, and project storage + retrieval

    :copyright: (c) 2012 by Mek
    :license: BSD, see LICENSE for more details.
"""

from datetime import datetime
from configs.config import DBNAME
from lazydb.lazydb import Db

PRIORITIES = ['Needs Triage', 'Wishlist', 'Low',
              'Normal', 'High', 'Unbreak Now!']
STATUSES = ['Open', 'In Progress', 'Resolved', 'Will Not Fix']

class LazyStore(object):

    KEY = None

    def __init__(self, key):
        self.key = key

    def insert(self):
        """Inserts this obj instance into lazydb and returns the
        index (its id) of the obj within in resultant list 
        """        
        db = Db('db/{}'.format(DBNAME))
        return db.append(self.key, self)

    def update(self):
        """TODO"""
        pass

    @classmethod
    def getall(cls):
        db = Db('db/{}'.format(DBNAME))
        return db.get(cls.KEY)

    @classmethod
    def get(cls, uid):
        return cls.getall()[int(uid)]    

    @classmethod
    def disable(cls, uid):
        db = Db('db/{}'.format(DBNAME))
        tickets = db.get(cls.KEY)
        tickets[int(uid)].enabled = False
        return db.put(cls.KEY, tickets)

class Task(LazyStore):

    KEY = 'task'

    def __init__(self, title, status_id=0, priority_id=0, desc='', project_id=None,
                 owner_id=None, date=datetime.now().ctime(), enabled=True):
        """Entries are never deleted, they are just flagged as
        enabled=0 and skipped. This way, we can guarantee the objs id
        based on its index in the value list within lazydb
        """
        super(Task, self).__init__(key=self.KEY)
        self.title = title
        self.description = desc
        self.date = date
        self.status_id = int(status_id)
        self.priority_id = int(priority_id)
        self.project_id = int(project_id)
        self.owner_id = int(owner_id)
        self.enabled = enabled

class User(LazyStore):

    KEY = 'user'

    def __init__(self, name, username, email, enabled=True):
        super(User, self).__init__(key=self.KEY)
        self.name = name
        self.username = username
        self.email = email
        self.enabled = enabled

class Project(LazyStore):

    KEY = 'project'

    def __init__(self, name, enabled=True):
        super(Project, self).__init__(key=self.KEY)
        self.name = name
        self.enabled = enabled
