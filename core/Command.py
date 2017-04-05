from .ModuleParser import ModuleParser

class Command:
    # parse all modules (?)

    __commands = {}

    # depends on ModuleParser
    @classmethod
    def register(cls, name, clb, parser=lambda: {}):
        (module, command) = name.split(':')

        if command not in cls.__commands:
            cls.__commands[command] = {
                'modules': [{module: {'clb': clb, 'parser': parser}}]
            }
        else:
            cls.__commands[command]['modules'].append({module: {'clb': clb, 'parser': parser}})

    @classmethod
    def list(cls):
        return cls.__commands

    @classmethod
    def call(cls, command, module, params):
        if command not in cls.__commands:
            raise Exception('Command {} not found.'.format(command))

        m = cls.__commands[command][module]

        m['clb']( m['parser'](params) )


# get current module
# class Module():
#     @classmethod
#     def init(cls):
#         return { 'depends': []
#                , 'params': []
#                , 'commands': []
#                }


# moduledir:
#     - init.py
#     ...modulefiles

# OR

# modulefile.py

# init.py/modulefile.py:

# Command.register(name, callback_func, {
#     'arg': {
#         required: true #assume false if not present
#     ,   name: 'argname'
#     ,   default: 'defvalue'
#     ,   depends: ['modules', 'dependency', 'for', 'this', 'command']
#     }
# })

# manifest.yml:

# commands:
#     commname:
#         callback

# args:
#     argname:
#         required:
#         name:
#             longname
#             sname

#     argname:
#         optional:
#         name:
#             longname
#             sname
#         default:
#             007

