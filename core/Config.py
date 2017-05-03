import os, imp, yaml, logging
from .Command import Args

class Config():
    
    container = {
        'root': 'Groot',
        'abspath': os.path.realpath(os.path.basename(__file__) + '/../'),
    }

    _isInited = False


    @classmethod
    def parseEnv(cls):

        configData = {}

        configFile = cls.container.get('abspath') + '/.env'
        configData = cls.getDataFromFile(configFile)

        if not configData:
            return
            
        #todo str to uppercase
        for key in configData:
            if key in os.environ:
                cls.container[key] = os.environ[key]
            else:
                cls.container[key] = configData[key]

        return cls.container


    @classmethod
    def get(cls, key):
        if not cls._isInited:
            cls.parseEnv()
            cls._isInited = True

        # if not exists in container system vars
        if key in cls.container:
            return cls.container[key]
        elif key in os.environ:
            return os.environ[key]
        else:
            return False


    @classmethod
    def _import(cls, module, filePath):
        # filepath from module name replace . to /
        try:
            package = imp.load_source(module, filePath)
        except:
            return False

        return package


    @classmethod
    def getDataFromFile(cls, fileName):

        fileDict = {}

        if( not os.path.isfile(fileName) ):
            return False

        fileData = open(fileName)

        for line in fileData.readlines():

            line = line.rstrip('\n')

            listData = line.split('=')

            if len(listData) == 2:
                key = listData[0]
                value = listData[1]
                fileDict[key] = value;
                

        fileData.close()

        return fileDict

    @classmethod
    def loadConfigFile(cls, path):
        if os.path.isfile(path):
            with open(path, 'r') as f:
                ymlConf = yaml.load(f)

                if 'modules' in ymlConf:
                    for m in ymlConf['modules']:
                        if m in ymlConf:
                            ymlConf[m] = Args(ymlConf[m])

                return ymlConf if ymlConf is not None else {}

        return {}

    @classmethod
    def saveConfigFile(cls, path, data):
        with open(path, 'w') as f:
            return yaml.dump(data, f, default_flow_style=False)

