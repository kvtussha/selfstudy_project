from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from materials.forms import CourseForm
from materials.models import Course


class MainView(TemplateView):
    template_name = 'main_page.html'


class ContactView(TemplateView):
    template_name = 'contacts.html'


class CourseListView(ListView):
    model = Course
    template_name = 'courses/courses_list.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_object(self, queryset=None):
        self.course = super().get_object(queryset)
        return self.course


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('materials:all_courses')
    template_name = 'courses/course_form.html'


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'

    def get_success_url(self):
        return reverse('materials:course_detail', kwargs={'pk': self.object.pk})


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('materials:all_courses')
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление курса'
        return context