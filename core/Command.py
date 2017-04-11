from .ModuleParser import ModuleParser
import logging, sys, os, traceback

from itertools import chain

class CommandObserver:
    __commands = {}

    @classmethod
    def register(cls, name, clb, parser=lambda x: {}):
        (module, command) = name.split(':')

        if command not in cls.__commands:
            cls.__commands[command] = Command(command)

        cmd = cls.__commands[command]
        cmd.addModule(module, clb, parser)       

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
        return cmd.parseArgs(args)

    @classmethod
    def execute(cls, command, args):
        if command not in cls.__commands:
            raise Exception('Cannot execute command {}. Command not found.'.format(command))

        cmd = cls.__commands[command]
        res = cmd.execute(args)

        if not res:
            print('Command execution process failure')
            return False

        return True


class Command:
    name = None
    modules = {}
    execModules = []

    def __init__(self, name):
        self.name = name
        self.modules = {}
        self.execModules = []

    def __repr__(self):
        modules = list( self.modules.keys() )
        return 'Command {}; modules: {};'.format(self.name, ', '.join(modules))

    def addModule(self, module, clb, parser):
        self.modules[module] = {
            'clb': clb,
            'parser': parser
        }

    def parseArgs(self, inputList):

        margs = []
        for i in inputList.module:
            margs.extend(i)

        res = {}

        for marg in margs:
            try:
                argsList = marg.split(' ')

                m = argsList[0]
                res[m] = self.modules[m]['parser'](argsList[1:])
                self.execModules.append(m)
            except KeyError:
                print('Module {} not found'.format(m))

        return res

    def execute(self, args):
        m = None
        try:
            if self.execModules == []: self.execModules = self.modules
            for m in self.execModules:
                clb = self.modules[m]['clb']
                clb(args)

                print( 'Module {} ... done'.format(m) )

            return True

        except Exception as e:
            logging.debug('Module %s error: %s', m, e)
            print('Module {} error: {}', m, e)
            # need additional info about what's exactly going wrong
            # traceback.print_stack()
            return False

        finally:
            self.execModules = []



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

