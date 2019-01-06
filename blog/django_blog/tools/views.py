from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def tools_list(request):
    #return HttpResponse('tools')
    return render(request, 'tools/tools_list.html')
