
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import *
from .email import SendEmail

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,)


def home(request):
    if request.method == 'POST':
        name = request.POST['fName']
        company = request.POST['company']
        email = request.POST['email']
        phone = request.POST['phone']
        question = request.POST['question']
        new_msg = Message(name=name, company=company, email=email, phone=phone, question=question)
        new_msg.save()
        SendEmail(name, company, email, phone, question)
        return redirect('home')
    else:
        return render(request, 'home.html')


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders.html'

    def get_queryset(self):
        return reversed(Order.objects.all())


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'create_order.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('orders')


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'check_order.html'

    def get_success_url(self):
        return reverse('orders')


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'delete_order.html'

    def get_success_url(self):
        return reverse('orders')


def linksToTables(request):
    return render(request, 'links_to_tables.html')


class TruckListView(LoginRequiredMixin, ListView):
    model = Truck
    context_object_name = 'trucks'
    template_name = 'trucks.html'


class TruckCreateView(LoginRequiredMixin, CreateView):
    model = Truck
    template_name = 'create_truck.html'
    form_class = TruckForm

    def get_success_url(self):
        return reverse('trucks')


class TruckUpdateView(LoginRequiredMixin, UpdateView):
    model = Truck
    form_class = TruckForm
    template_name = 'update_truck.html'

    def get_success_url(self):
        return reverse('trucks')


class TruckDeleteView(LoginRequiredMixin, DeleteView):
    model = Truck
    template_name = 'delete_truck.html'

    def get_success_url(self):
        return reverse('trucks')


class TrailerListView(LoginRequiredMixin, ListView):
    model = Trailer
    context_object_name = 'trailers'
    template_name = 'trailers.html'


class TrailerCreateView(LoginRequiredMixin, CreateView):
    model = Trailer
    template_name = 'create_trailer.html'
    form_class = TrailerForm

    def get_success_url(self):
        return reverse('trailers')


class TrailerUpdateView(LoginRequiredMixin, UpdateView):
    model = Trailer
    form_class = TrailerForm
    template_name = 'update_trailer.html'

    def get_success_url(self):
        return reverse('trailers')


class TrailerDeleteView(LoginRequiredMixin, DeleteView):
    model = Trailer
    template_name = 'delete_trailer.html'

    def get_success_url(self):
        return reverse('trailers')


class DriverListView(LoginRequiredMixin, ListView):
    model = Driver
    context_object_name = 'drivers'
    template_name = 'drivers.html'


class DriverCreateView(LoginRequiredMixin, CreateView):
    model = Driver
    template_name = 'create_driver.html'
    form_class = DriverForm

    def get_success_url(self):
        return reverse('drivers')


class DriverUpdateView(LoginRequiredMixin, UpdateView):
    model = Driver
    form_class = DriverForm
    template_name = 'update_driver.html'

    def get_success_url(self):
        return reverse('drivers')


class DriverDeleteView(LoginRequiredMixin, DeleteView):
    model = Driver
    template_name = 'delete_driver.html'

    def get_success_url(self):
        return reverse('drivers')


class CargoesListView(LoginRequiredMixin, ListView):
    model = Cargo
    context_object_name = 'cargoes'
    template_name = 'cargoes.html'


class CargoesCreateView(LoginRequiredMixin, CreateView):
    model = Cargo
    template_name = 'create_cargo.html'
    form_class = CargoForm

    def get_success_url(self):
        return reverse('cargoes')


class CargoesUpdateView(LoginRequiredMixin, UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'update_cargo.html'

    def get_success_url(self):
        return reverse('cargoes')


class CargoesDeleteView(LoginRequiredMixin, DeleteView):
    model = Cargo
    template_name = 'delete_cargo.html'

    def get_success_url(self):
        return reverse('cargoes')


class AddressListView(LoginRequiredMixin, ListView):
    model = DeliveryAddress
    context_object_name = 'addresses'
    template_name = 'addresses.html'


class AddressCreateView(LoginRequiredMixin, CreateView):
    model = DeliveryAddress
    template_name = 'create_address.html'
    form_class = AddressForm

    def get_success_url(self):
        return reverse('addresses')


class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = DeliveryAddress
    form_class = AddressForm
    template_name = 'update_address.html'

    def get_success_url(self):
        return reverse('addresses')


class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = DeliveryAddress
    template_name = 'delete_address.html'

    def get_success_url(self):
        return reverse('addresses')


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'customers.html'


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = 'create_customer.html'
    form_class = CustomerForm

    def get_success_url(self):
        return reverse('customers')


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'update_customer.html'

    def get_success_url(self):
        return reverse('customers')


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'delete_customer.html'

    def get_success_url(self):
        return reverse('customers')


class OrderItemListView(LoginRequiredMixin, ListView):
    model = OrderItem
    context_object_name = 'orderlines'
    template_name = 'orderlines.html'


class OrderItemDetailView(DetailView):
    model = OrderItem
    template_name = 'orderlines_details.html'


class OrderItemUpdateView(LoginRequiredMixin, UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'orderlines_update.html'

    def get_success_url(self):
        return reverse('orderlines_details', kwargs={'pk': self.object.id})


class OrderItemDeleteView(LoginRequiredMixin, DeleteView):
    model = OrderItem
    template_name = 'orderlines_delete.html'
    success_url = "/orderlines"


class OrderItemCreateView(LoginRequiredMixin, CreateView):
    model = OrderItem
    template_name = 'orderlines_create.html'
    form_class = OrderItemForm
    success_url = "/orderlines"


class UploadsListView(LoginRequiredMixin, ListView):
    model = Upload
    context_object_name = 'files'
    template_name = 'uploads.html'


class UploadsCreateView(LoginRequiredMixin, CreateView):
    model = Upload
    template_name = 'add_file.html'
    form_class = FilesForm

    def get_success_url(self):
        return reverse('uploads')


def delete_item(request, pk):
    if request.method == 'POST':
        item = Upload.objects.get(pk=pk)
        item.delete()
    return redirect('uploads')


class MessagesListView(LoginRequiredMixin, ListView):
    model = Message
    context_object_name = 'messages'
    template_name = 'messages.html'


class MessagesDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'delete_message.html'
    success_url = "/messages"


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile saved")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)

