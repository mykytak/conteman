import os, sys, imp, yaml
from functools import reduce

sys.path.insert(0, os.path.abspath('../core'))
from core.Config import Config
from core.Command import CommandObserver

class ModuleParser():
    # parse modules

    @classmethod
    def parse(cls):
        moddir = os.path.join(Config.get('conteman_dir'), 'modules')
        modules = os.listdir(moddir)

        for m in modules:

            if os.path.isfile(os.path.join(moddir, m)): continue

            modpath = os.path.join(moddir, m)
            modinit = os.path.join(modpath, 'init.py' )

            with open(os.path.join(modpath, 'config.yml')) as f:
                config = yaml.load(f)
                # add result to Config

                if config is None or 'commands' not in config: continue

                package = imp.load_source(m, modinit)

                for key in config['commands']:
                    cmd = config['commands'][key]

                    func = reduce( lambda obj, attr: getattr(obj, attr, None),
                                    cmd['func'].split('.'),
                                    package
                                    )

                    if not callable(func):
                        raise Exception('Wrong commands field. Command {} function not found'.format(cmd['func']))

                    CommandObserver.register(cmd['name'], func)


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
