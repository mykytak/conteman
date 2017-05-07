import argparse, os, sys
from subprocess import call

sys.path.insert(0, os.path.abspath('../core'))
from core.Command import CommandObserver

def register():
    CommandObserver.register('sublime:create' , Sublime.create)
    CommandObserver.register('sublime:open'   , Sublime.open)
    CommandObserver.register('sublime:update' , Sublime.update)

class Sublime():
    @staticmethod
    def parser(x):
        main = argparse.ArgumentParser()
        main.add_argument('-s', '--shortcut', default='subl') # sublime console shortcut.
        main.add_argument('-n', '--name') # subl project name
        main.add_argument('-p', '--path') # subl project path
        return main.parse_args(x)


    @staticmethod
    def extract(state):
        name = state.name if state.sublime.name is None else state.sublime.name
        name += '.sublime-project'
        path = state.sublime.path if state.sublime.path is not None else \
                '{state.path}/{state.conf_dir}'.format(state=state)

        return (path, name)


    @classmethod
    def create(cls, state):
        (path, name) = cls.extract(state)

        mode = 0o775

        with open(path + '/' + name, 'w') as f:
            print('{{"folders":[{{"path": "{}"}}]}}'.format(state.path), file=f)

    @classmethod
    def update(cls, state):
        (path, name) = cls.extract(state)

        # project already exist
        if os.path.isfile(path + '/' + name):
            return

        cls.create(state)


    @classmethod
    def open(cls, state):
        (path, name) = cls.extract(state)

        cmd = '{state.sublime.shortcut} --project {path}/{name}'.format(state=state, path=path, name=name)
        call(cmd, shell=True)
