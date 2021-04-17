from django.shortcuts import render
from django.utils import timezone

from memo import forms, models


class Handler:

    def __init__(self):
        self.f_request = None
        self.f_parameters: dict = {}

    @property
    def request(self):
        return self.f_request

    @property
    def parameters(self) -> dict:
        return self.f_parameters

    @request.setter
    def request(self, arg):
        self.f_request = arg

    @parameters.setter
    def parameters(self, arg: dict):
        self.f_parameters = arg

    def run(self):
        pass


class TitleListHandler(Handler):

    def __init__(self):
        super().__init__()

    def run(self):
        nodes = models.Node.objects.all()
        nodes = list(map(lambda node: dict(id=node.id, title=node.title, date=node.date), nodes))
        params = {
            'nodes': nodes,
            'form': forms.Node(None),
        }
        return render(self.request, 'memo/page/list.html', params)


class NodeHandler(Handler):

    def __init__(self):
        super().__init__()

    def run(self):
        node = models.Node.objects.filter(id=self.parameters['node_id']).first()
        params = {
            'title': node.title,
            'text': node.text,
            'date': node.date,
            'form': forms.Node(None),
        }
        return render(self.request, 'memo/page/node.html', params)


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
        models.Node.objects.filter(id=self.request.POST['id']).delete()
        t = TitleListHandler()
        t.request = self.request
        return t.run()
