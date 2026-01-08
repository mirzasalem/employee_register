from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.models import User
from django.contrib import messages

def employee_list(request):
    context = {'employee_list' : Employee.objects.all()}
    return render(request,"employee_register/employee_list.html", context)


def employee_login(request):
    # context = {'employee_login' : Employee.objects.all()}
    return render(request,"employee_register/login.html")

def employee_register(request):
    
    if request.method== "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            
            messages.info(request, "Already Exists.")
            return redirect ('/employee/register/')
            # return redirect ('/')
            
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            # password = password
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Created successfully")
        return redirect ('/employee/register/')
    
    
    # context = {'employee_list' : Employee.objects.all()}
    return render(request,"employee_register/register.html")


def employee_form(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = EmployeeForm()
        else:
            employee= Employee.objects.get(pk=id)
            form= EmployeeForm(instance= employee)
        return render(request,"employee_register/employee_form.html",{'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee= Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')
    
    # form = EmployeeForm()
    # return render(request,"employee_register/employee_form.html",{'form':form})



def employee_delete(request, id):
    employee= Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')