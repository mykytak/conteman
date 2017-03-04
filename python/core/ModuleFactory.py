import imp, os, sys

sys.path.insert(0, os.path.abspath('../core'))
from core.InteractiveShell import InteractiveShell 

class ModuleFactory():

    @staticmethod
    def broadcast(action, modules, state = None):

        for m in modules:
            try:
                package = imp.load_source(m, state.climp_dir + '/modules/' + m + '.py')
                cls = getattr(package, m.title())
                if action in dir(cls):

                    if 'properties' in cls.__dict__:
                        shell = InteractiveShell.get(cls.properties(), m)
                    
                    # return
                    # if shell, merge with state.m
                    act = getattr(cls, action)
                    act(state)
            except (ImportError, FileNotFoundError) as e:
                print("Module {} not found. {}".format(m, e))

        InteractiveShell.write(state.base_dir + '/' + state.projname)
