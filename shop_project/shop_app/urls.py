from django.urls import path
from . import views

app_name = 'shop_app'

urlpatterns = [
  path('', views.index, name='index'),
  path('search/<str:value>', views.search, name='search'),
  path('search/', views.index, name='search'),
  path('products/<int:product_id>', views.product, name='product'),
  path('customers/', views.customers, name='customers'),
  path('customers/<int:customer_id>', views.customer, name='customer'),
  path('maillots/', views.maillots, name='maillots'),
  path('maillots/<int:maillot>', views.maillot, name='maillot'),
  path('products/<int:product_id>/comment_form', views.comment_form, name='comment_form'),
  path('products/<int:product_id>/question_form', views.question_form, name='question_form'),
  path('questions/<int:question_id>/response_form', views.response_form, name='response_form'),
  path('comments/<int:comment_id>/comment_response_form', views.comment_response_form, name='comment_response_form'),

]