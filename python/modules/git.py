import os, sys

# https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options
# https://docs.python.org/3/library/argparse.html#sub-commands
# https://habrahabr.ru/post/301532/

from subprocess import getoutput, call, check_output, CalledProcessError

# from .base import *

def _call(projpath, command = None):
    if command is None:
        return lambda x: _call(projpath, x)

    call("cd {}; {}".format(projpath, command), shell=True)

def create(state):
    projname = state.projname

    conf = {
        'base_dir': '/home/xedar/devel'
      , 'username': 'Mykytak'
      , 'email': 'mykytak.ua@gmail.com'
    }


    folder = os.path.realpath( conf['base_dir'] + '/' + projname )

    callFunc = _call(folder)

    try:
        output = getoutput("git init {}".format(folder))
        callFunc("git config user.name {}".format(conf['username']))
        callFunc("git config user.email {}".format(conf['email']))
        print( output )
    except CalledProcessError as e:
        print( e.output )


    print('git create with state: {}'.format(state))
