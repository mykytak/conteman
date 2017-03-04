import imp, os

class ModuleFactory():

    @staticmethod
    def broadcast(action, modules, state = None):
        # @todo: add module hash map

        for m in modules:
            try:
                package = imp.load_source(m, '/home/xedar/devel/workflowScripts/python/modules/' + m + '.py')
                cls = getattr(package, m.title())
                if action in dir(cls):
                    act = getattr(cls, action)
                    act(state)
            except (ImportError, FileNotFoundError) as e:
                print("Module {} not found. {}".format(m, e))

