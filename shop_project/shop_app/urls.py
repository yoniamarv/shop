from django.urls import path
from . import views

app_name = 'shop_app'

urlpatterns = [
  path('', views.index, name='index'),
  path('products/<int:product_id>', views.product, name='product'),
  path('customers/', views.customers, name='customers'),
  path('customers/<int:customer_id>', views.customer, name='customer'),
  path('products/<int:product_id>/comment_form', views.comment_form, name='comment_form'),
  path('maillots/', views.maillots, name='maillots'),
  path('maillots/<int:maillot>', views.maillot, name='maillot'),
]