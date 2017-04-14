import os, sys, yaml, argparse

sys.path.insert(0, os.path.abspath('../core'))
from core.Config import Config
from core.Command import *
import logging

class State():
    globconf = {}
    contextconf = {}

    moduleArgs = {}

    # name = None
    # path = ''
    # command = None

    def __init__(self, args):

        # @todo: parse ~/.conteman
        if os.path.isfile('~/.conteman/conteman.yml'):
            self.globconf = Config.fromYml('~/.conteman/conteman.yml')

        if not Config.get('base_dir'):     raise KeyError("you must specify base_dir")
        if not Config.get('conf_dir'):     raise KeyError("you must specify conf_dir")
        if not Config.get('conteman_dir'): raise KeyError("you must specify conteman_dir")

        if args.name:
            if '/' in args.name:
                temp = args.name.split('/')
                self.name = temp[-1]
            else:
                self.name = args.name

            self.path = os.path.realpath( Config.get('base_dir') + '/' + args.name )

        self.command = args.command

        self.parse_args(args)

        if args.name: self.contextconf = Config.loadConfigFile(self.path + '/conteman.yml')

        logging.debug(self.contextconf)

    def parse_args(self, args):
        parsed = CommandObserver.parseCmdArgs(self.command, args)


        self.moduleArgs = parsed

        logging.debug('Parsed module args: %s', self.moduleArgs)

    def __getattr__(self, name):
        """
        Search order:
        1. module conf from command line
        2  context name, path and current command
        3. local context config file
        4. from environment
        5. global context config file
        ?  Run interactive mode if enabled ?
        6. None
        """
        if (name == 'name' or name == 'path') and (name not in self.__dict__ or not self.name):
            raise Exception('This command requires project name.')

        if name in self.moduleArgs:
            return self.moduleArgs[name]

        if name in self.contextconf: return self.contextconf[name]


        attr = Config.get(name)
        if attr: return attr

        if name in self.globconf: return getattr(self.globconf, name)

        # run interactive mode

        return None

    def save(self, type):
        """
        Save current config state.
        type can be: local, global
        """

        path = self.path + '/conteman.yml' if type == 'local' else '~/.conteman/conteman.yml'

        # merge context config with modules config
        data = self.prepareLocalConfig() if type == 'local' else self.prepareGlobalConfig()

        Config.saveConfigFile(path, data)


    def prepareLocalConfig(self):
        for key, value in self.moduleArgs.items():
            self.contextconf[key] = vars(value) if isinstance(value, argparse.Namespace) else value

        return self.contextconf

        # self.moduleArgs
        # Command.modules

