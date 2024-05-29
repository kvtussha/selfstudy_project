from django.urls import path

from materials.views import CourseListView

app_name = 'materials'

urlpatterns = [
    path('', CourseListView.as_view(), name='all-courses'),
]
