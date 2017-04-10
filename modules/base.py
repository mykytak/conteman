import os, sys, yaml, argparse

sys.path.insert(0, os.path.abspath('../core'))
from core.Command import CommandObserver


def register():
    CommandObserver.register('base:create', BaseModule.create)

class BaseModule():
    # action for configure project before start
    def prepare(self):
        pass

    @classmethod
    def create(cls, state):
        path = state.base_dir + '/' + state.projname
        mode = 0o775

        # if os.path.exists(projpath):
        #     raise Exception("project already exist. Use 'add' or 'open'.")

        for f in ['/', '/src', '/db', '/doc', '/' + state.conf_dir, '/tests']:
            if os.path.exists(path + f): continue
            os.makedirs(path + f, mode)  


        # project configuration stored here.
        # something similar to node/bower configuration. Take options for modules, their configs etc.
        # open(projpath + '/.proj.json', 'a').close()

        if state.modules is None == 1:
            return #no modules passed

        # broadcast action to modules
        # factory.broadcast('create', state.modules, state)

        # add record to db


    @classmethod
    def add(cls, state):
        for prop in state.projconf:
            if prop in state.modules:
                state.modules.remove(prop)
        if len(state.modules) == 0:
            print('No modules to install')
        else:
            # factory.broadcast('create', state.modules, state)
            pass


    @classmethod
    def open(cls, state):
        # factory.broadcast('open', state.modules, state)
        pass
        # run .projopen

    def archive(self):
        pass

# modules: python package, every file in that package - action
