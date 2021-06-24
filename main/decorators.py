from django.http import HttpResponse
from django.shortcuts import redirect 
def unauthenticated_user(view_func):
    def wrapper_funct(request, *args , **kwargs):
        if request.user.is_authenticated:
            return redirect('home') 
        else :
            return view_func(request, *args , **kwargs)
    return wrapper_funct

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_funct(request, *args , **kwargs):
            print('Working here',allowed_roles)
            group = None 
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args , **kwargs)
            else:
                return HttpResponse('you cant see that page ')
        return wrapper_funct 
    return decorator