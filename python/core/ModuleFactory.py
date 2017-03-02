import imp, os

class ModuleFactory():

    @staticmethod
    def broadcast(action, modules, args = []):
        # @todo: add module hash map

        for m in modules:
            try:
                package = imp.load_source(m, '/home/xedar/devel/workflowScripts/python/modules/' + m + '.py')
                if action in dir(package):
                    act = getattr(package, action)
                    act(args)
            except (ImportError, FileNotFoundError) as e:
                print("Module {} not found.".format(m))

