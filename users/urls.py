from django.urls import path
from users import views
  
urlpatterns = [
    path('manage_role/<int:erp>', views.manage_role.as_view()),
    path('manage_role/<int:erp>/<int:user_type>', views.manage_role.as_view()),
    path('user_list/', views.UserList.as_view()),
]
  
