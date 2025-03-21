from django import forms
from .models import Employee 


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee  # Ensure this is your correct model
        fields = ('fullname','mobile','emp_code','position')  # Fixed spelling
        labels = {
                'fullname':'Full Name',
                'emp_code':'EMP.Code'
        }

