
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.index,name="index"),
   path('get_question/',views.questions,name='questions'), 
   path('questions/',views.questions, name='questions'),
   path('timerexpired/',views.timer_expired,name="time-expired"), 
   path('allparticipants/',views.allparticipants,name="allparticipants"),
   path('leaderboard/',views.leaderboard,name="leaderboard"),
]
