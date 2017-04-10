import os, sys, yaml

sys.path.insert(0, os.path.abspath('../core'))
from core.Config import Config
from core.Command import *
import logging

class State():
    projconf = {}
    moduleArgs = {}

    path = ''
    name = None
    command = None

    def __init__(self, args):

        # @todo: parse ~/.conteman

        if not Config.get('base_dir'):     raise KeyError("you must specify base_dir")
        if not Config.get('conf_dir'):     raise KeyError("you must specify conf_dir")
        if not Config.get('conteman_dir'): raise KeyError("you must specify conteman_dir")

        if args.name:
            self.path = os.path.realpath( Config.get('base_dir') + '/' + args.name )
            self.name = args.name

        self.command = args.command

        self.parse_args(args)

        return
        
        if os.path.isfile(args.path + '/conteman.yml'):
            with open(args.path + '/conteman.yml', 'r') as f:
                ymlConf = yaml.load(f)
                if ymlConf is not None:
                    self.projconf = ymlConf

    def parse_args(self, args):
        parsed = CommandObserver.parseCmdArgs(self.command, args)

        self.moduleArgs = parsed


    def __getattr__(self, name, default = None):
        if name == 'name' and not self.name:
            raise Exception('This command requires project name.')

        if name in self.moduleArgs:
            return self.moduleArgs[name]

        try:
            return self.projconf[name]
        except (KeyError, TypeError):
            attr = None

        attr = Config.get(name)

        return attr if attr else default
