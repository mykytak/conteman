class Router():
    # inst = None

    # def __init__(self, routes={}):
    #     self.routes = routes

    # @classmethod
    # def _instance(cls):
    #     if cls.inst is None:
    #         cls.inst = Router()

    #     return cls.inst

    _routes = {}

    @classmethod
    def route(cls, name, func):
        # inst = cls._instance()
        cls._routes[name] = func

    @classmethod
    def routes(cls, rts):
        # inst = cls._instance()

        for name in rts:
            cls._routes[name] = rts[name]

    @classmethod
    def action(cls, inp):
        if isinstance(inp, str):
            inp = inp.split()

            if len(inp) == 1: inp.append(' ')

        name, *args = inp

        if callable(name in cls._routes and cls._routes[name]):
            return cls._routes[name](args)

        raise Exception("Action not registered") # @maybe: usage() func
