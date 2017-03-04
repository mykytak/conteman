import imp, os, sys, yaml


class InteractiveShell():
    configs = {}
    choices = {}

    def __set__(self, name, value):
        self.choices.name = value


    # def __init__(self):
    @classmethod
    def get(cls, props, module):
        cls.build_user_config(props, module)


    @classmethod
    def write(cls, path):
        with open(path + '/climp.yml', 'w') as outfile:
            yaml.dump(cls.configs, outfile, default_flow_style=False)


    @classmethod
    def build_user_config(cls, obj, module):

        cls.configs[module] = {}
        
        for prop in obj['required']:
            
            cls.configs[module][prop] = input(obj['required'][prop] + ": ")


        return
