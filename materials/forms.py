from django.forms import ModelForm

from materials.models import Course


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'course_topics')
