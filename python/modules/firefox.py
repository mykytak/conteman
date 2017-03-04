from subprocess import call, getoutput

# https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options

class Firefox():
    @staticmethod
    def create(state):
        mode = 0o775

        name = state.projname
        path = state.path + '/' + state.conf_dir

        cmd = 'firefox -CreateProfile -no-remote "{} {}"'.format(name, path + '/firefox_' + name)

        print( getoutput(cmd) )

    def open(state):
        name = state.projname
        cmd = 'firefox -P "{}" -no-remote &'.format(name)
        call(cmd, shell=True)
