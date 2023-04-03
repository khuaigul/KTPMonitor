from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response        

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        print(request.path)
        if "registration" in request.path or "profileData" in request.path:
            return response        
        if request.user.has_perm('content.' + request.path):
           print('jkl')
           return response
        else:
           print('hjk')
           return render(request, 'main/main.html')

        # Code to be executed for each request/response after
        # the view is called.

        return response