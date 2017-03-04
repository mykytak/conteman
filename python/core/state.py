import os, sys

sys.path.insert(0, os.path.abspath('../core'))
from core.Config import Config

class State():
    internals = {}

    def __init__(self, args):

        # @todo: parse ~/.clipmrc
        # @todo: parse projdir/.climprc

        if not Config.get('base_dir'):  raise KeyError("you must specify base_dir")
        if not Config.get('conf_dir'):  raise KeyError("you must specify conf_dir")
        if not Config.get('clipm_dir'): raise KeyError("you must specify clipm_dir")
        
        args.path = os.path.realpath( Config.get('base_dir') + '/' + args.projname )

        self.args = args


    def __getattr__(self, name):
        attr = getattr(self.args, name, None)

        if attr is not None: return attr

        attr = Config.get(name)

        if not attr: return None

        return attr
