from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",index,name='index'),
    path("login_attempt/",login_attempt,name='login_attempt'),
    path("register_customer/",register_customer,name='register_customer'),
    path("register_labour/",register_labour,name='register_labour'),
    path("customer/",customer,name='customer'),
    path("labour/",labour,name='labour'),
    path('verify/<auth_token>',verify,name='verify'),
    path('book/<int:customer_id>/<int:labour_id>/', book, name='book'),
    path('lab_cart/',lab_cart,name='lab_cart')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

