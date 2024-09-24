from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User_table
# Create your views here.


def user_table(request):
    table = {'table': User_table.objects.all()}
    return render(request, "admin_dashboard/user_table.html", table)

def user_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = UserForm()
        else:
            user_entry = User_table.objects.get(pk=id)
            form = UserForm(instance=user_entry)
        return render(request, "admin_dashboard/user_form.html", {'form':form})
    else:
        if id==0:
            form = UserForm(request.POST)
        else:
            user_entry = User_table.objects.get(pk=id)
            form = UserForm(request.POST, instance=user_entry)
        if form.is_valid():
            form.save()
        return redirect("/user/table")
        

def user_delete(request, id=-1):
    user_entry = User_table.objects.get(pk=id)
    user_entry.delete()
    return redirect("/user/table")