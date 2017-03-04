import os, sys

# https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options
# https://docs.python.org/3/library/argparse.html#sub-commands
# https://habrahabr.ru/post/301532/

from subprocess import getoutput, call, check_output, CalledProcessError

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

    @classmethod
    def create(cls, state):
        projname = state.projname

        conf = {
            'username': 'Mykytak'
          , 'email': 'mykytak.ua@gmail.com'
        }

        callFunc = cls._call(state.path)

        try:
            output = getoutput("git init {}".format(state.path))
            callFunc("git config user.name {}".format(conf['username']))
            callFunc("git config user.email {}".format(conf['email']))
            with open("{}".format(state.path + '/.gitignore'), 'w') as f:
                ignore = state.conf_dir + '\ndoc'
                print( ignore, file=f )

            callFunc("git add .; git commit -m 'initial'")

            print( output )
        except CalledProcessError as e:
            print( e.output )


        print('git create with state: {}'.format(state))
