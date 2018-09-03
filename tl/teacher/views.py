from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def do_1(request):
    return HttpResponse('this is a test')
def do_2(request, year, month):
    return HttpResponse('the date is {}-{}'.format(year, month))

def book_page(r, pn):
    return HttpResponse("the page number is {}".format(pn))

def name(r,name):
    return HttpResponse("my name is {}".format(name))


def index(r):
    #render 第一个参数是request，第二个是html
    return render(r, 'index.html')

def do_render(r):
    #第三个参数是context，key要和html中{{name}}对应
    return render(r,"render.html",{"name":"charry"})
#第三种方法
def do_render2(r):
    t = loader.get_template("render2.html")

    r = t.render({"name": "charry2"})

    return  HttpResponse(r)