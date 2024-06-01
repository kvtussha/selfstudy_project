from django.contrib import admin

from django.contrib import admin

from materials.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'create_date',
                    'image', 'owner')
    list_filter = ('title', 'create_date')

