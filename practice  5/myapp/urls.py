# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Basic CRUD operations
    path('', views.index, name='index'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),

    # Expense-related views
    path('expenses/', views.expense_list, name='expense_list'),

    # Category views
    path('categories/add/', views.add_category, name='add_category'),

    # Group expense views
    path('group-expenses/add/', views.add_group_expense, name='add_group_expense'),
    path('group-expenses/', views.group_expense_list, name='group_expense_list'),
]