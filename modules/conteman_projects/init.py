import os,sys, yaml, argparse, logging

class ContemanProjects():
    @classmethod
    def create(cls, state):
        if os.path.exists(state.path):
            raise Exception('Project folder already exist.')

        mode = 0o775

        print(state.path)
        print(state.config_dir)

        for f in ['/', '/src', '/db', '/doc', '/' + state.config_dir, '/tests']:
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

