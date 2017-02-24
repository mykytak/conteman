import os, sys

from subprocess import getoutput, call, check_output, CalledProcessError

from .base import *

class GitModule(BaseModule):

    # stype - storage type
    # types: github, bitbucket. @maybe: raw, gitlab
    # proj: obj of Project type
    def __init__(self, stype, proj):
        self.type = stype
        self.proj = proj

    def enable(self):
        folder = os.path.realpath( self.proj.base_dir + '/' + self.proj.name )

        try:
            # @todo: check if repo already exist

            output = getoutput("git init {}".format(folder))
            call("cd {}; git config user.name {}".format(folder, self.proj.username), shell=True)
            call("cd {}; git config user.email {}".format(folder, self.proj.email), shell=True)
            print( output )

        except CalledProcessError as exc:
            print( exc.output )


    # def disable(self):
