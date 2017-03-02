import os

def create(args):
    name = args.projname

    conf = {
        'base_dir': '/home/xedar/devel'
    }

    path = os.path.realpath( conf['base_dir'] + '/' + name )

    mode = 0o775

    with open(path + '/.climp/{}.sublime-project'.format(name), 'w') as f:
        print('{{"folders":[{{"path": "{}"}}]}}'.format(path), file=f)


    # if os.path.exists(projpath):
    #     raise Exception("project already exist. Use 'add' or 'open'.")

    # for f in ['/', '/src', '/db', '/doc']:
    #     os.makedirs(projpath + f, mode)

def open(args): pass
    # subl --project .climp/test_new.sublime-project
