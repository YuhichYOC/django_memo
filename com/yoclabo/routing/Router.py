from com.yoclabo.routing import Handler


class Router:

    def __init__(self):
        self.f_request = None
        self.f_parameters: list = []

    @property
    def request(self):
        return self.f_request

    @property
    def parameters(self) -> list:
        return self.f_parameters

    @request.setter
    def request(self, arg):
        self.f_request = arg

    @parameters.setter
    def parameters(self, arg: list):
        self.f_parameters = arg

    def has_post(self) -> bool:
        return True if 0 < len(self.request.POST) else False

    def has(self, name: str) -> bool:
        if self.request.POST[name] is None:
            return False
        if 0 == len(self.request.POST[name]):
            return False
        return True

    def run_handler(self, arg: Handler.Handler):
        arg.request = self.request
        arg.parameters = self.parameters
        return arg.run()


class MemoRouter(Router):

    def __init__(self):
        super().__init__()

    def run(self):
        if self.has_post():
            if self.has('title'):
                if self.has('text'):
                    return self.run_handler(Handler.InsertHandler())
                pass
            pass
        return self.run_handler(Handler.TitleListHandler())
