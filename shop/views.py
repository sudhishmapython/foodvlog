from django.shortcuts import render,get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def view(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        prodt=product.objects.filter(categ=c_page,available=True)
    else:
        prodt=product.objects.all().filter(available=True)
    cat = category.objects.all()
    paginator=Paginator(prodt,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'pr':prodt,'ct':cat,'pg':pro})

def prodDetails(request,c_slug,pro_slug):
    try:
        prod=product.objects.get(categ__slug=c_slug,slug=pro_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'pd':prod})

def searching(request):
    prodd=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prodd=product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,"search.html",{'qr':query,'prs':prodd})
