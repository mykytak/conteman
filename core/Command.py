# from .ModuleParser import ModuleParser
import logging, sys, os, traceback, argparse

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
    def execute(cls, command, state):
        if command not in cls.__commands:
            raise Exception('Cannot execute command {}. Command not found.'.format(command))

        cmd = cls.__commands[command]
        res = cmd.execute(state)

        if not res:
            print('Command execution process failure')
            return False

        return True


class Args():
    def __init__(self, args = {}):
        self.args = args

    def __getattr__(self, name):
        # interactive shell here?
        return self.args if name in self.args else None

    def __setstate__(self, state):
        self.args = state

    def __getstate__(self):
        return vars(self.args) if isinstance(self.args, argparse.Namespace) else self.args

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
        self.execModules = []

        margs = []
        for i in inputList.module:
            margs.extend(i)

        res = {}

        for marg in margs:
            try:
                argsList = marg.split(' ')

                m = argsList[0]
                res[m] = Args( self.modules[m]['parser'](argsList[1:]) )
                self.execModules.append(m)
            except KeyError:
                print('Module {} not found'.format(m))

        return res

    def execute(self, state):
        m = None
        try:
            if self.execModules == []: self.execModules = self.modules

            for m in self.execModules:
                # this is bad. I don't remember why execModules was developed
                # but they must be changed in some way. They filled in Command.parse_args
                # and also exist in State.parse_args for some reason.
                # They must be filled in command only!
                if m not in self.modules: continue

                clb = self.modules[m]['clb']
                clb(state)

                print( 'Module {} ... done'.format(m) )

            return True

        except Exception as e:
            print('Module {} error: {};\n{}'.format(m, repr(e), traceback.format_exc()))
            return False

        finally:
            state.save('local')
            # save current config
