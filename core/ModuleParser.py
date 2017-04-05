import os, sys, imp

sys.path.insert(0, os.path.abspath('../core'))
from core.Config import Config


class ModuleParser():
    # parse modules
    # 

    @classmethod
    def parse(cls):
        moddir = os.path.join(Config.get('conteman_dir'), 'modules')
        modules = os.listdir(moddir)

        for m in modules:

            modpath = os.path.join(moddir, m)
            is_simple = os.path.isfile( modpath )

            if is_simple:
                package = imp.load_source(m, modpath)


                action = getattr(package, 'register', None)

                if callable(action):
                    action()
            else:
                print('You can use only one-file modules right now.')
                continue

                modpath = os.path.join(modpath, 'init.py' )
                # print(modpath, m)
                # exit()

                package = imp.load_source(m + '/init.py', modpath)

                print(package)


# @staticmethod
#     def broadcast(action, modules, state = None):
#         for m in modules:
#             try:
#                 package = imp.load_source(m, state.conteman_dir + '/modules/' + m + '.py')
#                 cls = getattr(package, m.title())
#                 if action in dir(cls):

#                     shell = None
#                     if action == 'create' and 'properties' in cls.__dict__:
#                         shell = InteractiveShell.build_user_config(cls.properties(), m)

#                     # if shell, merge with state.m
#                     if shell is not None:
#                         setattr(state, m, shell)

#                     act = getattr(cls, action)
#                     act(state)
#             except (ImportError, FileNotFoundError) as e:
#                 print("Module {} not found. {}".format(m, e))

#         if action == 'create':
#             InteractiveShell.write(state.base_dir + '/' + state.projname, state.projconf)