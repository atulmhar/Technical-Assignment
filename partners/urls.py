from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin login route
    path('login/', views.login_view, name='login'),

    # Admin logout route (uses Django's built-in logout view)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Dashboard route (requires login)
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Partner management routes
    path('partners/', views.partner_list_view, name='partner_list'),  # Partner listing
    path('partners/add/', views.add_partner_view, name='add_partner'),  # Add new partner
    path('partners/<int:pk>/', views.partner_detail_view, name='partner_detail'),  # Partner details
    path('partners/edit/<int:pk>/', views.edit_partner_view, name='edit_partner'),  # Edit partner
]
