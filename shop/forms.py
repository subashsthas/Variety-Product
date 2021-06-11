from django import forms
from .models import Customer, Product, Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('username','customer_shopPic', 'customer_shopName', 'customer_Pan', 'customer_address', 'customer_district', 'customer_proporator',
                  'customer_proporatorMobile',
                  'customer_contactPerson', 'customer_contactPersonMobile', 'customer_shopNumber',
                  'customer_residentPhone',
                  'customer_Transportation')
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email', 'phone', 'desc')

class CrudForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_image', 'product_category', 'unit_Of_Product', 'product_rate', 'product_details')

class NewForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


