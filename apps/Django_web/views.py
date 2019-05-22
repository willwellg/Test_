from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import ListView
from .models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import xlrd

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/index.html'


def first_page(request):
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

def uploade(request):
    if request == 'POST':
        myform = FileUploadForm(request.POST, request.FILES)

        if myform.is_valid():
            f = request.FILES

            wb = xlrd.open_workbook(filename=None, file_content=f.read())
            table = wb.sheet()[0]
            nrow = table.nrows
            ncol = table.ncols
            print(nrow, ncol)

            for i in range(1, nrow+1):
                row_value = table.row_value(i)
                st = Article()
                id = row_value.rowvalue[1]
                title = row_value.rowvalue[2]
                author = row_value.rowvalue[3]
                st.title = title
                st.author = author
                st.save()
    return HttpResponseRedirect("http://127.0.0.1:8000/query")


def upload_excel(request):

    return render_to_response('base/uplaod_excel.html')






