import imp, os, sys

sys.path.insert(0, os.path.abspath('../core'))
from core.InteractiveShell import InteractiveShell 

class ModuleFactory():

    @staticmethod
    def broadcast(action, modules, state = None):
        print(action)
        for m in modules:
            try:
                package = imp.load_source(m, state.climp_dir + '/modules/' + m + '.py')
                cls = getattr(package, m.title())
                if action in dir(cls):

                    if action == 'create' and 'properties' in cls.__dict__:
                        shell = InteractiveShell.build_user_config(cls.properties(), m)

                    # if shell, merge with state.m
                    if shell is not None:
                        setattr(state, m, shell)

                    act = getattr(cls, action)
                    act(state)
            except (ImportError, FileNotFoundError) as e:
                print("Module {} not found. {}".format(m, e))

        if action == 'create':
            InteractiveShell.write(state.base_dir + '/' + state.projname)
