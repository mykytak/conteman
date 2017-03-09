import os, sys, yaml

sys.path.insert(0, os.path.abspath('../core'))
from core.Config import Config

class State():
    projconf = {}

    def __init__(self, args):

        # @todo: parse ~/.conteman

        if not Config.get('base_dir'):  raise KeyError("you must specify base_dir")
        if not Config.get('conf_dir'):  raise KeyError("you must specify conf_dir")
        if not Config.get('conteman_dir'): raise KeyError("you must specify conteman_dir")

        args.path = os.path.realpath( Config.get('base_dir') + '/' + args.projname )
        
        if os.path.isfile(args.path + '/conteman.yml'):
            with open(args.path + '/conteman.yml', 'r') as f:
                ymlConf = yaml.load(f)
                if ymlConf is not None:
                    self.projconf = ymlConf

        self.args = args


    def __getattr__(self, name, default = None):
        attr = getattr(self.args, name, None)

        if attr is not None: return attr

        try:
            return self.projconf[name]
        except (KeyError, TypeError):
            attr = None

        attr = Config.get(name)

        return attr if attr else default
