from .ModuleParser import ModuleParser

class Command:
    # parse all modules (?)

    __commands = {}

    # depends on ModuleParser
    @classmethod
    def register(cls, name, clb, args={}):
        (module, command) = name.split(':')

        if command not in cls.__commands:
            cls.__commands[command] = {
                'modules': [{module: {'clb': clb, 'args': args}}]
            }
        else:
            cls.__commands[command]['modules'].append({module: {'clb': clb, 'args': args}})

    @classmethod
    def list(cls):
        return cls.__commands

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

