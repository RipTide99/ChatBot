from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import Forminfo
from .models import Query_table


# Create your views here.

def home(request):
    return render(request,'Admin_page.html')

def admin_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = Forminfo()
        else:
            row = Query_table.objects.get(pk = id)
            form = Forminfo(instance=row)
        return render(request,'form.html',{'form': form})
    else:
        if id == 0:
            form = Forminfo(request.POST)
        else:
            row = Query_table.objects.get(pk = id)
            form = Forminfo(request.POST, instance=row)
        if form.is_valid():
            form.save()
        return redirect('/admin_list')

def admin_list(request):
    context = {'que_list':Query_table.objects.all()}
    return render(request,'list.html',context)

def admin_delete(request,id):
    row = Query_table.objects.get(pk = id)
    row.delete()
    return redirect('/admin_list')



