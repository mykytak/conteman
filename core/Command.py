from .ModuleParser import ModuleParser
import logging

class CommandObserver:
    __commands = {}

    @classmethod
    def register(cls, name, clb, parser=lambda: {}):
        (module, command) = name.split(':')

        if command not in cls.__commands:
            cls.__commands[command] = Command(command)

        cls.__commands[command].addModule(module, clb, parser)       

    @classmethod
    def list(cls):
        return cls.__commands

    @classmethod
    def call(cls, command, module, params):
        if command not in cls.__commands:
            raise Exception('Command {} not found.'.format(command))

        m = cls.__commands[command][module]

        m['clb']( m['parser'](params) )

    @classmethod
    def parseCmdArgs(cls, command, args):
        if command not in cls.__commands:
            raise Exception('Command {} not found.'.format(command))

        cmd = cls.__commands[command]
        cmd.parseArgs(args)


class Command:
    name = None
    modules = {}

    def __init__(self, name):
        self.name = name

    def addModule(self, module, clb, parser):
        self.modules[module] = {
            clb: clb,
            parser: parser
        }

    def parseArgs(self, inputList):
        margs = inputList.module

        for marg in margs:
            try:
                argsList = marg[0].split(' ')
                m = argsList[0]
                self.args[m] = self.modules[m][parser](argsList)
            except KeyError:
                print('Module {} not found'.format(m))

        return True


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

