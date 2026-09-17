# i have created this file - om
from urllib import request

from django.http import HttpResponse
from django.shortcuts import render
# day 6
def index(request):

    return render(request,'index.html')

# def about(request):
#     return HttpResponse("hello om bhai")

def analyser(request):
    djtext = request.GET.get('text', 'default')
    removepunch = request.GET.get('removepunch','off')

    print(djtext)
    print(removepunch)
    if removepunch == "on":
        #analyse = djtext
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
        analyse = ""
        for char in djtext:
            if char not in punctuation:
                analyse = analyse + char
        param ={'porpose':'remove punctuation', 'analyse_text':analyse}
        return render( request,'analyser.html',param)
    # return render(request, 'index.html')
    else:
        return HttpResponse("error")

    return HttpResponse('''<h1>hello world</h1> <a href="https://chatgpt.com/c/6aa9843d-4124-83ee-aa25-00ed68664375">chatgpt</a>'''
    '''<a href='/'>front</a>''')

# def removepuch(request):
#     return HttpResponse('''remove puch <a href="capitlizefirst">front</a>'''
#                         '''<a href =''>back</a>''')
#
# def capitlizefirst(request):
#     return HttpResponse( '''capitlizefirst  <a href="newlineremover">front</a>'''
#                          '''<a href = "removepuch">back</a>''')
#
# def newlineremover(requsest):
#     return HttpResponse('''newlineremover  <a href="spaceremover">front</a>'''
#                         '''<a href = "capitilizerfirst">back</a>''')
#
# def spaceremover(request):
#     return HttpResponse('''spaceremover  <a href="charcount">front</a>'''
#                         '''<a href = "newlineremover">back</a>''')
#
# def charcount(request):
#     return HttpResponse('''charcount <a href = "spaceremover">back</a>''')
