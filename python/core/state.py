class State():
    internals = {}

    def __init__(self, args):
        self.args = args

        # @todo: parse ~/.clipmrc
        # @todo: parse projdir/.climprc
        self.internals = {
            'base_dir': '/home/xedar/devel'
        }

    def __getattr__(self, name):
        attr = getattr(self.args, name, None)

        if attr is not None: return attr

        try:
            return self.internals[name]
        except KeyError:
            return None
