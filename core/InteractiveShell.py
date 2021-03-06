import imp, os, sys, yaml


class InteractiveShell():
    configs = {}
    choices = {}

    def __set__(self, name, value):
        self.choices.name = value


    @classmethod
    def write(cls, path, projconf=None):

        if projconf is not None:
            cls.configs.update(projconf)

        with open(path + '/conteman.yml', 'w') as outfile:
            yaml.dump(cls.configs, outfile, default_flow_style=False)


    @classmethod
    def build_user_config(cls, obj, module):

        cls.configs[module] = {}
        if 'required' in obj:
            for prop in obj['required']:
                cls.configs[module][prop] = input(obj['required'][prop] + ": ")

        if 'default' in obj:
            for prop in obj['default']:
                cls.configs[module][prop] = obj['default'][prop]

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

