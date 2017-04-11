import sys, os
from subprocess import call, getoutput

sys.path.insert(0, os.path.abspath('../core'))
from core.Command import CommandObserver

# https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options

def register():
    CommandObserver.register('firefox:create', Firefox.create)

class Firefox():
    @staticmethod
    def create(state):
        mode = 0o775

        path = state.path + '/' + state.conf_dir

        # check if state.name already registered as firefox profile.
        cmd = 'firefox -CreateProfile -no-remote "{} {}"'.format(state.name, path + '/firefox_' + state.name)

        print( getoutput(cmd) )


    @staticmethod
    def properties():
        return {
            "default": {
                "exists": "true"
            }
        }


    def open(state):
        cmd = 'firefox -P "{}" -no-remote &'.format(state.name)
        call(cmd, shell=True)
