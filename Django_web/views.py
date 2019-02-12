from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Article
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def queryAll(request):
    b = Article.objects.all()
    return render_to_response('base/Queryall.html', {'data': b})

def delByID(request):
    i = request.GET['id']
    bb = Article.objects.get(id = i)
    bb.delete()
    return HttpResponseRedirect("http://127.0.0.1:8000/query")

def addByID(request):
    return render_to_response('base/add.html')

def add(request):
    id = request.POST['id']
    title = request.POST['title']
    author = request.POST['author']
    st = Article()
    if len(id) > 0:
        st.id = id
    st.title = title
    st.author = author
    st.save()
    return HttpResponseRedirect("http://127.0.0.1:8000/query")

def updateByID(requst):
    i = requst.GET['id']
    b = Article.objects.get(id = str(i))
    return render_to_response('base/update.html', {'data': b})
