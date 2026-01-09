from django import forms
from .models import Employee
from django.conf import settings
from django.core.mail import send_mail
class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ('fullname', 'emp_code','mobile', 'position')
        labels = {
            'fullname' : 'Full Name',
            'emp_code' : 'Employee Code'
        }
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False
        
        
def send_registration_email(to_email, username):
    subject = "Welcome to Employee System"
    message = f"Hello {username},\n\nYour account has been created successfully."
    from_email = "admin@example.com"

    send_mail(
        subject,
        message,
        from_email,
        [to_email],
        fail_silently=False,
    )