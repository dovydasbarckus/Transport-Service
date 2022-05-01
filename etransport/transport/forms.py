
from .models import *
from django import forms
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = fields = '__all__'
        widgets = {
            'invoice': forms.TextInput(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'date_ordered': DateInput(attrs={'class': 'form-control'}),
        }


class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = fields = '__all__'
        widgets = {
            'truck_brand': forms.TextInput(attrs={'class': 'form-control'}),
            'truck_model': forms.TextInput(attrs={'class': 'form-control'}),
            'truck_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'truck_year': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TrailerForm(forms.ModelForm):
    class Meta:
        model = Trailer
        fields = fields = '__all__'
        widgets = {
            'trailer_brand': forms.TextInput(attrs={'class': 'form-control'}),
            'trailer_model': forms.TextInput(attrs={'class': 'form-control'}),
            'trailer_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'trailer_year': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = fields = '__all__'
        widgets = {
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'dimensions': forms.TextInput(attrs={'class': 'form-control'}),
            'dangerous': forms.TextInput(attrs={'class': 'form-control'}),
            'information': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = DeliveryAddress
        fields = fields = '__all__'
        widgets = {
            'delivery_address': forms.TextInput(attrs={'class': 'form-control'}),
            'loading_address': forms.TextInput(attrs={'class': 'form-control'}),
            'custom_address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = fields = '__all__'
        widgets = {
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'order': forms.Select(attrs={'class': 'form-control'}),
            'truck': forms.Select(attrs={'class': 'form-control'}),
            'trailer': forms.Select(attrs={'class': 'form-control'}),
            'driver': forms.Select(attrs={'class': 'form-control'}),
            'delivery_address': forms.Select(attrs={'class': 'form-control'}),
            'date_delivery': DateInput(attrs={'class': 'form-control'}),
            'date_loading': DateInput(attrs={'class': 'form-control'}),
            'delivery_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'information': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class FilesForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('name', 'file', 'order_item')
        widgets = {
            'order_item': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }