import os

class State():
    internals = {}

    def __init__(self, args):

        # @todo: parse ~/.clipmrc
        # @todo: parse projdir/.climprc
        self.internals = {
            'base_dir': '/home/xedar/devel'
          , 'conf_dir': '.clipm'
        }
        
        args.path = os.path.realpath( self.internals['base_dir'] + '/' + args.projname )

        self.args = args


    def __getattr__(self, name):
        attr = getattr(self.args, name, None)

        if attr is not None: return attr

        try:
            return self.internals[name]
        except KeyError:
            return None
