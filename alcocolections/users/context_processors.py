from bottle.utils import menu

def get_bottle_context(request):
    return {'mainmenu': menu}