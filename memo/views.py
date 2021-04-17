from com.yoclabo.routing import Router


def browse(request):
    r = Router.MemoRouter()
    r.request = request
    return r.run()


def browse_node(request, node_id):
    r = Router.MemoRouter()
    r.request = request
    r.parameters['node_id'] = node_id
    return r.run()
