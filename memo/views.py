from com.yoclabo.routing import Router


def browse(request):
    r = Router.MemoRouter()
    r.request = request
    return r.run()
