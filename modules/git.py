import os, sys, argparse, logging

# https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options
# https://docs.python.org/3/library/argparse.html#sub-commands
# https://habrahabr.ru/post/301532/

sys.path.insert(0, os.path.abspath('../core'))
from core.Command import CommandObserver

from subprocess import getoutput, call, check_output, CalledProcessError

def register():
    CommandObserver.register('git:create', Git.create, Git.parser)
    CommandObserver.register('git:update', Git.update, Git.parser)

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
    def parser(x):
        main = argparse.ArgumentParser()
        main.add_argument('-u', '--user')
        main.add_argument('-e', '--email')
        return main.parse_args(x)

    @classmethod
    def create(cls, state):
        projname = state.name

        callFunc = cls._call(state.path)

        try:
            output = getoutput("git init {}".format(state.path))
            callFunc("git config user.name {state.git.user}".format(state=state))
            callFunc("git config user.email {state.git.email}".format(state=state))
            with open("{}".format(state.path + '/.gitignore'), 'w') as f:
                ignore = state.conf_dir + '\ndoc'
                f.write(ignore)

            callFunc("git add .; git commit -m 'initial'")

            logging.debug( output )
        except CalledProcessError as e:
            logging.debug( e.output )


        print('git create with state: {}'.format(state))


    @classmethod
    def update(cls, state):

        user = getoutput("cd {}; git config user.name".format(state.path))
        email = getoutput("cd {}; git config user.email".format(state.path))

        if user and email:
            state.git.user = user
            state.git.email = email
            return

        callFunc = cls._call(state.path)

        if user is None and state.git.user is not None:
            callFunc("git config user.name {state.git.user}".format(state=state))

        if email is None and state.git.email is not None:
            callFunc("git config user.email {state.git.email}".format(state=state))

