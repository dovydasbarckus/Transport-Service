from django.contrib import admin
from .models import Truck, Trailer, Customer, Cargo, Driver, DeliveryAddress, Order, OrderItem, Profile, Upload


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('truck', 'trailer', 'driver', 'delivery_address', 'date_delivery', 'date_loading', 'delivery_price',
                                        'quantity', 'information')


admin.site.register(Profile)
admin.site.register(Truck)
admin.site.register(Trailer)
admin.site.register(Customer)
admin.site.register(Cargo)
admin.site.register(Driver)
admin.site.register(DeliveryAddress)
admin.site.register(Order)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Upload)
