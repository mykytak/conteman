from subprocess import call

class Sublime():
    @staticmethod
    def create(state):
        name = state.projname

        mode = 0o775

        with open(state.path + '/' + state.conf_dir + '/{}.sublime-project'.format(name), 'w') as f:
            print('{{"folders":[{{"path": "{}"}}]}}'.format(state.path), file=f)


        # if os.path.exists(projpath):
        #     raise Exception("project already exist. Use 'add' or 'open'.")

        # for f in ['/', '/src', '/db', '/doc']:
        #     os.makedirs(projpath + f, mode)

    @staticmethod
    def open(state):
        cmd = 'subl --project {}/{}.sublime-project'.format(state.conf_dir, state.projname)
        call(cmd, shell=True)
