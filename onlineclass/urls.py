from django.urls import path
from onlineclass import views

urlpatterns = [
    path('schedule/', views.OnlineClassSchedule.as_view()),
    path('join/<int:schedule_id>/', views.JoinLog.as_view()),
    path('join/<int:schedule_id>/<int:log_status>/', views.JoinLog.as_view()),
    path('statistics/<int:schedule_id>/', views.ClassLog.as_view()),
]