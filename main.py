#!/usr/bin/python3

from core.ModuleParser import ModuleParser
from core.Command import *
from core.Config import Config
from core.state import State

import logging, argparse, sys

logging.basicConfig( level=logging.DEBUG
                   , format='[%(asctime)s %(filename)s:%(lineno)d] %(message)s'
                   )

ModuleParser.parse()

parser = argparse.ArgumentParser()
parser.add_argument('command')
parser.add_argument('name', nargs='?')
parser.add_argument('-m', '--module', nargs='*', default=[], action='append')

args = parser.parse_args()

state = State(args)

res = CommandObserver.execute(args.command, state)

if res:
    print('Done!')
else:
    print('Failure.')

# main.py create proj -m firefox name:myfox -m sublime 

exit()


import argparse, sys, yaml

from modules.base import BaseModule as base
from core.state import State
from core.Config import Config



def set_default_subparser(self, name, args=None):
    """default subparser selection. Call after setup, just before parse_args()
    name: is the name of the subparser to call by default
    args: if set is the argument list handed to parse_args()

    , tested with 2.7, 3.2, 3.3, 3.4
    it works with 2.6 assuming argparse is installed
    """
    subparser_found = False
    for arg in sys.argv[1:]:
        if arg in ['-h', '--help']:  # global help if no subparser
            break
    else:
        for x in self._subparsers._actions:
            if not isinstance(x, argparse._SubParsersAction):
                continue
            for sp_name in x._name_parser_map.keys():
                if sp_name in sys.argv[1:]:
                    subparser_found = True
        if not subparser_found:
            # insert default in first position, this implies no
            # global options without a sub_parsers specified
            if args is None:
                sys.argv.insert(1, name)
            else:
                args.insert(0, name)


Config.parseEnv()

argparse.ArgumentParser.set_default_subparser = set_default_subparser

root = argparse.ArgumentParser()
parsers = root.add_subparsers()


def test(args):
    print('main with ', args)
main = parsers.add_parser('proj')

# parse modules
# add yml with enabled modules
# form actions

actions = ['create', 'add', 'open', 'archive']
main.add_argument('contextname', help="Context name (name of the project for example)")
main.add_argument('action', help="Action: {}".format('|'.join(actions)), choices=actions)

main.add_argument('-m', '--module', nargs='*', default=None) # -m module1 arg1 -m module2 -m module3 arg1 arg2 arg3
main.add_argument('-ms', '--modules', default=None) # -ms module1 module2 module3

main.set_defaults(cls=base)

modules = parsers.add_parser('module')
modules.add_argument('name')
modules.add_argument('action')
modules.set_defaults(cls='Some random text here')


root.set_default_subparser('proj')
args = root.parse_args()

# _parse_known_args


action = getattr(args.cls, args.action)
state = State(args)

projname = args.projname.split('/')
if len(projname) > 1:
    for d in projname[:-1]:
        state.base_dir += '/' + d

    state.projname = projname[-1]

action(state)







# proj = ModuleFactory.get('main', args)

# proj.action('create')





# gitModule = GitModule('git', proj)


# Router.routes({
#         'create': lambda args: print(1)
#     })

# Router.action('create')


"""

proj create projname modules:
    call route(create, params) #params: [projname, modules]
        create folder structure
        create and call modules, save them etc.

proj open projname:

"""






# DB.exec("CREATE TABLE test (id int, name text)")

# db.exec("CREATE TABLE templates (id int, name text, modules text")
# db.exec("CREATE TABLE projects (id int, template_id int, config text, created_at text, updated_at text")

# db.exec("CREATE TABLE modules (id int, name text, priority int)")


"""
actions:
    create projname [template]
        folder structure, init vagrant, init bitbucket/github repo and push, firefox session
        create projopen script:
        open sublime project, firefox, check new commits on remote, up and ssh to vagrant

        templates: modules to be included.

    create-manually projname [modules]
        same as create but include only folder structure by default.
        Any additional modules can be passed as parameters
       
    open
        run projopen script
   
    archive
        push
        gzip
        move to (?)

    assign [modules]
        move existing project into system




    modules:
        subtree with modules operations

        Modules has priorities. Modules with lower number in priority runs at first.

        current modules:
            - git @maybe: bitbucket/github/raw custom scripts (?)
            - vagrant
            - firefox
            - sublime

        @maybe:
            - heroku
            - testings (A/B, slow load, high load, run local tests, etc)

        update [modulename] priority

        enable/disable [modulename]

"""

# project
# db:
#   folder
#   last_access
# config:
#   ide: sublime | tmux
#   openAs
#   openScript: "init shell scripts"
# folder structure:
#   .git
#   src
#     -- Vagrantfile
#   db   <-- optional
#   doc <-- optional
#   .projopen <-- autogenerated bash script
#   





# $1 -> project name

# open existing project
# go to project dir (~/devel/proj_name)
# open firefox profile
# run vagrant
# open sublime project
# save pids for fox and sublime

# new project
# create vagrant
# create new fox profile
# create new sublime project
# create git
# create bitbucket (?)
# new trello/jira board (?)

# archive project
# move all to bitbucket
# move all to some archive folder (files dir, fox profile, sublime project)
# remove fox profile from available
# delete vagrant vm. Probably backup some data firstly