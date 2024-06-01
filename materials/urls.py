from django.urls import path

from materials.views import CourseListView, ContactView, MainView, CourseDetailView, CourseCreateView, CourseDeleteView, \
    CourseUpdateView

app_name = 'materials'

urlpatterns = [
    path('', MainView.as_view(), name='main_page'),
    path('contacts/', ContactView.as_view(), name='contacts'),

    path('courses/', CourseListView.as_view(), name='all_courses'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course/create/', CourseCreateView.as_view(), name='course_create'),
    path('course/update/<int:pk>/', CourseUpdateView.as_view(), name='course_update'),
    path('course/delete/<int:pk>/', CourseDeleteView.as_view(), name='course_delete'),
]
