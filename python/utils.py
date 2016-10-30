import shelve

DB_FILE = '/home/xedar/devel/workflowScripts/python/db.shelve'
CRONTAB = '/var/spool/cron/crontabs/walrus'

"""
db structure:
  state - current state.
          working - don't show any popups except urgent
                    show state popups
  cron  - what jobs must be enabled with what state

"""

class State():
    def __init__(self, name, allowed = 'all'):
        self.name    = name
        self.allowed = allowed if isinstance(allowed, list) else [allowed]

    def allow(self, name):
        self.allowed.append(name)

    def can(self, name):
        return True if name in self.allowed else False

# def Manager():
