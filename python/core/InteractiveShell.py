import imp, os, sys, yaml


class InteractiveShell():
    configs = {}
    choices = {}

    def __set__(self, name, value):
        self.choices.name = value


    # def __init__(self):
    @classmethod
    def get(cls, props, module):
        return cls.build_user_config(props, module)


    @classmethod
    def write(cls, path):
        with open(path + '/climp.yml', 'w') as outfile:
            yaml.dump(cls.configs, outfile, default_flow_style=False)


    @classmethod
    def build_user_config(cls, obj, module):

        cls.configs[module] = {}
        
        for prop in obj['required']:
            
            cls.configs[module][prop] = input(obj['required'][prop] + ": ")

        print(cls.configs[module])
        return cls.configs[module]


    @classmethod
    def update_user_config(cls, path, module, key, value):
        with open('test.yml', 'r') as f:
            test = yaml.load(f)
            test['host'] = 'huyuber.com'

            with open('test.yml', 'r+') as f:
                line = f.readline()
                offset = 0

                inputStr = 'host: api.huyuber.com'

                # for i, line in enumerate(f):
                while line:
                    if line.strip() == 'host: api.uber.com':
                        temp = f.tell()

                        f.seek( offset )

                        _f = open('test.yml', 'rb+')

                        _f.seek( temp - 1 )
                        tail = _f.read()
                        
                        f.write(inputStr)

                        f.truncate( f.tell() )

                        _f.seek( f.tell() )
                        _f.write(tail)

                        _f.close()
                            

                    offset = f.tell()
                    line = f.readline()
                    # else:
                    #     f.write(line)

            f.close()