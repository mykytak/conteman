import os, sys, yaml

sys.path.insert(0, os.path.abspath('../core'))
from core.ModuleFactory import ModuleFactory as factory

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

        # open(path + '/.propen', 'a').close()
        # with open(path + '/climp.yml', 'w') as outfile:
        #     yaml.dump(configs, outfile, default_flow_style=False)        


        # project configuration stored here.
        # something similar to node/bower configuration. Take options for modules, their configs etc.
        # open(projpath + '/.proj.json', 'a').close()

        if state.modules is None == 1:
            return #no modules passed

        # broadcast action to modules
        factory.broadcast('create', state.modules, state)

        # add record to db

    @classmethod
    def add(cls, state):
        print('addd', state.__dict__)

    @classmethod
    def open(cls, state):
        factory.broadcast('open', state.modules, state)
        # run .projopen

    def archive(self):
        pass

# modules: python package, every file in that package - action

