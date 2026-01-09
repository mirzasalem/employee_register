from django.shortcuts import render, redirect
from .forms import EmployeeForm, send_registration_email
from .models import Employee
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required , permission_required
from django.db.models import Q
from django.http import HttpResponseForbidden


@login_required(login_url= "/employee/login/")


# def my_view(request):

def employee_list(request):
    query = request.GET.get('search', '')  # default empty string
    # if not request.user.groups.filter(name='admin').exists():
    #     return HttpResponseForbidden("You are not authorized to s.Emailview this page.")

    if query:
        employees = Employee.objects.filter(Q(fullname__icontains=query))
        context = {
            'employee_list': employees,
            'search_query': query
        }
        return render(request, "employee_register/employee_list.html", context)
    else:
        employees = Employee.objects.all()
        context = {
            'employee_list': employees,
            'search_query': query  # empty string, not None
        }
        return render(request, "employee_register/employee_list.html", context)


def employee_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/employee/list/')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('/employee/login/')

    return render(request, "employee_register/login.html")

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
        # send_registration_email(
        #     to_email=user.email if user.email else "test@example.com",
        #     username=username
        # )
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
    if not request.user.is_staff:
        messages.error(request, "You are not authorized to delete employees.")
        return redirect('/employee/list')
    employee= Employee.objects.get(pk=id)
    employee.delete()
    messages.success(request, "Employee deleted successfully.")
    return redirect('/employee/list')

def log_out(request):
    logout(request)
    return redirect('/employee/login/')