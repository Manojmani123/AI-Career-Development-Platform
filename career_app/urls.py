from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('super-admin-dashboard/', views.super_admin_dashboard_view, name='super_admin_dashboard'),
    path('add-job-role/', views.add_job_role, name='add_job_role'),
    path('view-job-roles/', views.view_job_roles, name='view_job_roles'),
    path('add-skill/', views.add_skill, name='add_skill'),
    path('view-skills/', views.view_skills, name='view_skills'),
    path('assign-skills/', views.assign_skills_to_role, name='assign_skills_to_role'),
    path('view-role-skills/', views.view_role_skills, name='view_role_skills'),
    path('add-learning-resource/', views.add_learning_resource, name='add_learning_resource'),
    path('view-learning-resources/', views.view_learning_resources, name='view_learning_resources'),
]