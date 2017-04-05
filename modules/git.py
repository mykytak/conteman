import os, sys, argparse

# https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options
# https://docs.python.org/3/library/argparse.html#sub-commands
# https://habrahabr.ru/post/301532/

sys.path.insert(0, os.path.abspath('../core'))
from core.Command import Command

from subprocess import getoutput, call, check_output, CalledProcessError

def register():
    Command.register('git:create', Git.create)

class Git():
    @classmethod
    def _call(cls, projpath, command = None):
        if command is None:
            return lambda x: cls._call(projpath, x)

        call("cd {}; {}".format(projpath, command), shell=True)

    @staticmethod
    def properties():
        return {
            "required": {
                "username": "Your git username",
                "email": "Your git email"
            }
        }

    @staticmethod
    def parser():
        main = argparse.ArgumentParser()
        main.add_argument('-u', '--user')
        main.add_argument('-e', '--email')
        return lambda x: main.parse_args(x)

    @classmethod
    def create(cls, state):
        projname = state.projname

        callFunc = cls._call(state.path)
        print(state.__dict__)
        try:
            output = getoutput("git init {}".format(state.path))
            callFunc("git config user.name {state.git[username]}".format(state=state))
            callFunc("git config user.email {state.git[email]}".format(state=state))
            with open("{}".format(state.path + '/.gitignore'), 'w') as f:
                ignore = state.conf_dir + '\ndoc'
                print( ignore, file=f )

            callFunc("git add .; git commit -m 'initial'")

            print( output )
        except CalledProcessError as e:
            print( e.output )


        print('git create with state: {}'.format(state))
