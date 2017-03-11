import sys, os
from subprocess import call, getoutput

sys.path.insert(0, os.path.abspath('../core'))
from core.Command import Command

# https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options

def register():
    Command.register('firefox:create', Firefox.create)

class Firefox():
    @staticmethod
    def create(state):
        mode = 0o775

        name = state.projname
        path = state.path + '/' + state.conf_dir

        cmd = 'firefox -CreateProfile -no-remote "{} {}"'.format(name, path + '/firefox_' + name)

        print( getoutput(cmd) )


    @staticmethod
    def properties():
        return {
            "default": {
                "exists": "true"
            }
        }


    def open(state):
        name = state.projname
        cmd = 'firefox -P "{}" -no-remote &'.format(name)
        call(cmd, shell=True)
