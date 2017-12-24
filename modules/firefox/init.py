import sys, os, logging, argparse
from subprocess import call, getoutput

# https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options

class Firefox():
    @staticmethod
    def create(state):
        mode = 0o775

        name = state.firefox.name if state.firefox.name is not None else state.name
        path = state.firefox.path if state.firefox.path is not None else state.path + '/' + state.conf_dir

        # @todo: check if name already registered as firefox profile.
        cmd = 'firefox -CreateProfile -no-remote "{} {}"'.format(name, path + '/firefox/' + state.name)

        print( getoutput(cmd) )

    @staticmethod
    def update(state):
        # @todo: check if profile exist

        # profile name already passed. No need to create another one.
        # remove old profile if exist?
        if state.firefox.name is not None: return

        # create new profile
        Firefox.create(state)

    @staticmethod
    def parser(x):
        main = argparse.ArgumentParser()
        main.add_argument('-n', '--name') # profile name
        main.add_argument('-p', '--path') # profile path
        return main.parse_args(x)

    def open(state):
        logging.debug('opening firefox')
        profileName = state.name if state.firefox.name is None else state.firefox.name
        cmd = 'firefox -P "{}" -no-remote &'.format(profileName)
        call(cmd, shell=True)
