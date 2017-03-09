class Project():
    def __init__(self, name, modules = []):

        # merge:
        # user conf (from ~/.proj)
        # proj conf (from projdir/.proj)

        # bitbucket/git/github must be provided by git module
        modules = ['bitbucket', 'firefox', 'sublime', 'vagrant']

        self.name = name

        self.base_dir = '/home/xedar/devel'

        self.username = 'Mykytak'
        self.email    = 'mykytak.ua@gmail.com'

        self.modules = {}


    def action(self, action):
        # do something project-related with action
        # broadcast action to all modules
