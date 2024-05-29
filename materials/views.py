from django.views.generic import ListView

from materials.models import Course


class CourseListView(ListView):
    model = Course
    template_name = 'main_page.html'
    context_object_name = 'courses'
