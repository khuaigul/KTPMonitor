from django.shortcuts import render, redirect
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response        

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        # if request.user.has_perm(request.path):
        if request.user.is_authenticated:
            return response 
        else:
            return render(request, 'main/main.html')

        # Code to be executed for each request/response after
        # the view is called.

        return response