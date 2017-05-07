import os, sys, yaml, argparse, logging

sys.path.insert(0, os.path.abspath('../core'))
from core.Command import CommandObserver

# optional config for directories?
def register():
    CommandObserver.register('base:create', BaseModule.create)

class BaseModule():
    @classmethod
    def create(cls, state):
        if os.path.exists(state.path):
            # extend error message: use 'add' action or -f for forcing
            raise Exception('Project folder already exist.')

        mode = 0o775

        for f in ['/', '/src', '/db', '/doc', '/' + state.conf_dir, '/tests']:
            if os.path.exists(state.path + f): continue
            os.makedirs(state.path + f, mode)

    @classmethod
    def update(cls, state):
        # no update. Maybe use update if -f (--force) is present
        pass

    @classmethod
    def open(cls, state):
        # factory.broadcast('open', state.modules, state)
        pass
        # run .projopen

    def archive(self):
        pass

# modules: python package, every file in that package - action

