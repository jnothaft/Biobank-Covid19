from django.shortcuts import render
from django.http import HttpResponse

import time

# Create your views here.


def homePageView(request):
    """ Respond to an HTTP request with a simple web page."""
    print(request.user)
    response_html = '''
    <html>
    <h1>Hello, world!</h1>
    <p>
    This is our first application!
    </p>
    <hr>
    This page was generated at %s.
    </html>
    ''' % time.ctime()
    return HttpResponse(response_html)
