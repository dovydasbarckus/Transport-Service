from PIL import Image
from django.db import models
from django.contrib.auth.models import User
import datetime


class Truck(models.Model):
    truck_brand = models.CharField(max_length=200, null=True, blank=True)
    truck_model = models.CharField(max_length=200, null=True, blank=True)
    truck_plate = models.CharField(max_length=200, null=True, blank=True)
    truck_year = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Truck"
        verbose_name_plural = "Trucks"

    def __str__(self):
        return f'{self.truck_brand} : {self.truck_model} : {self.truck_plate}'


class Trailer(models.Model):
    trailer_brand = models.CharField(max_length=200, null=True, blank=True)
    trailer_model = models.CharField(max_length=200, null=True, blank=True)
    trailer_plate = models.CharField(max_length=200, null=True, blank=True)
    trailer_year = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Trailer"
        verbose_name_plural = "Trailers"

    def __str__(self):
        return f'{self.trailer_brand} : {self.trailer_model} : {self.trailer_plate}'


class Cargo(models.Model):
    cargo = models.CharField(max_length=200, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    dangerous = models.BooleanField(default=False, null=True, blank=True)
    dimensions = models.CharField(max_length=200, null=True, blank=True)
    information = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargoes"

    def __str__(self):
        return f'{self.cargo} : {self.weight}'


class Driver(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=200, null=True)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return f'{self.name} : {self.surname}'


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f'{self.name}  {self.surname} {self.company}'


class Order(models.Model):

    def number_default_function():
        timestamp = str(datetime.datetime.now().timestamp())
        invoice = timestamp.split(".")[0] + timestamp.split(".")[1]
        return invoice

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    date_ordered = models.DateField("Invoice issued", null=True, blank=True)
    invoice = models.CharField(max_length=100, null=True, blank=True, default=number_default_function)

    @property
    def total_sum(self):
        order_lines = OrderItem.objects.filter(order_id=self.id)
        total = 0
        for line in order_lines:
            total += line.delivery_price * line.quantity
        return total

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f'{self.id} --> {self.customer} '


class DeliveryAddress(models.Model):
    delivery_address = models.CharField(max_length=200, null=True)
    loading_address = models.CharField(max_length=200, null=True)
    custom_address = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Delivery and Loading Address"
        verbose_name_plural = "Delivery and Loading Address"

    def __str__(self):
        return f'{self.loading_address} : {self.delivery_address}'


class OrderItem(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    truck = models.ForeignKey(Truck, on_delete=models.SET_NULL, blank=True, null=True)
    trailer = models.ForeignKey(Trailer, on_delete=models.SET_NULL, blank=True, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, blank=True, null=True)
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.SET_NULL, blank=True, null=True)
    date_delivery = models.DateField("Date Delivery", null=True, blank=True)
    date_loading = models.DateField("Date Loading", null=True, blank=True)
    delivery_price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    information = models.TextField(max_length=200, null=True, blank=True)

    delivery_status = (
        ('N', "Not yet ordered"),
        ('O', "Order accepted"),
        ('C', "Carried out"),
        ('F', "Order finished"),
    )

    status = models.CharField(
        max_length=1,
        choices=delivery_status,
        blank=True,
        default='N',
        help_text="Status",
    )

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f' {self.cargo} : {self.order}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.photo.path)


class Upload(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.SET_NULL, blank=True, null=True)
    file = models.FileField(upload_to="files", blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Message(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    question = models.TextField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
