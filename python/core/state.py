import os, sys, yaml

sys.path.insert(0, os.path.abspath('../core'))
from core.Config import Config

class State():
    projconf = {}

    def __init__(self, args):

        # @todo: parse ~/.climprc

        if not Config.get('base_dir'):  raise KeyError("you must specify base_dir")
        if not Config.get('conf_dir'):  raise KeyError("you must specify conf_dir")
        if not Config.get('climp_dir'): raise KeyError("you must specify clipm_dir")

        args.path = os.path.realpath( Config.get('base_dir') + '/' + args.projname )

        if os.path.isfile(args.path + '/climp.yml'):
            with open(args.path + '/climp.yml', 'r') as f:
                ymlConf = yaml.load(f)
                if ymlConf is not None:
                    self.projconf = yaml.load(f)

        self.args = args


    def __getattr__(self, name):
        attr = getattr(self.args, name, None)

        if attr is not None: return attr

        try:
            return self.projconf[name]
        except (KeyError, TypeError):
            attr = None

        attr = Config.get(name)

        if not attr: return None

        return attr
