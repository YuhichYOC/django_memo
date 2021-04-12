from django.shortcuts import render
from django.utils import timezone

from memo import forms, models


class Handler:

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

    def value(self, name: str) -> str:
        return self.request.GET[name]

    def run(self):
        pass


class TitleListHandler(Handler):

    def __init__(self):
        super().__init__()

    def run(self):
        nodes = models.Node.objects.all()
        nodes = list(map(lambda node: dict(title=node.title, date=node.date), nodes))
        params = {
            'nodes': nodes,
            'form': forms.Node(None),
        }
        return render(self.request, 'memo/list.html', params)


class NodeHandler(Handler):

    def __init__(self):
        super().__init__()

    def run(self):
        node = models.Node.objects.filter(title=self.value('')).first()
        params = {
            'title': node.title,
            'text': node.text,
            'date': node.date,
            'form': forms.Node(None),
        }
        return render(self.request, 'memo/node.html', params)


class InsertHandler(Handler):

    def __init__(self):
        super().__init__()

    def run(self):
        n = models.Node()
        n.title = self.request.POST['title']
        n.text = self.request.POST['text']
        n.date = timezone.now()
        n.save()
        t = TitleListHandler()
        t.request = self.request
        return t.run()


class DeleteHandler(Handler):

    def __init__(self):
        super().__init__()

    def run(self):
        models.Node.objects.filter(title=self.request.POST['title']).delete()
        t = TitleListHandler()
        t.request = self.request
        return t.run()
