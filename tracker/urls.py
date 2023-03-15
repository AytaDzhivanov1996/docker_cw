from django.urls import path

from tracker.views import MyHabitListAPIView, PublicHabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, \
    HabitRetrieveAPIView, HabitDestroyAPIView

urlpatterns = [
    path('my_habit_list/', MyHabitListAPIView.as_view()),
    path('public_habit_list/', PublicHabitListAPIView.as_view()),
    path('create_habit/', HabitCreateAPIView.as_view()),
    path('update_habit/<int:pk>/', HabitUpdateAPIView.as_view()),
    path('retrieve_habit/<int:pk>/', HabitRetrieveAPIView.as_view()),
    path('destroy_habit/<int:pk>/', HabitDestroyAPIView.as_view()),
]