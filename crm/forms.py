from django import forms
from .models import Customer, Product, Service
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_name', 'organization', 'role', 'bldgroom', 'account_number', 'address', 
                      'city', 'state', 'zipcode', 'email','phone_number')

class ServiceForm(forms.ModelForm):
    class Meta:
       model = Service
       fields = ('cust_name', 'service_category', 'description', 'location', 'setup_time', 'cleanup_time', 'service_charge' )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('cust_name', 'product', 'p_description', 'quantity', 'pickup_time', 'charge', 'created_date')

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
	    model = User
	    fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
	    user = super(NewUserForm, self).save(commit=False)
	    user.email = self.cleaned_data['email']
	    if commit:
		    user.save()
	    return user

