from django.urls import path
from . import views

app_name = 'profile_app'

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('login/', views.login_auth, name='login'),
  path('profile/<int:user_id>/', views.profile, name='profile'),
  path('profile/<int:user_id>/edit/', views.edit_profile, name='edit_profile'),
  path('logout/', views.logout_view, name='logout_view')

]