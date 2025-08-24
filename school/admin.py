from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'get_teachers')
    list_filter = ('group', 'teachers')
    search_fields = ('name', 'group')
    
    def get_teachers(self, obj):
        return ", ".join([f"{teacher.name} ({teacher.subject})" for teacher in obj.teachers.all()])
    get_teachers.short_description = 'Преподаватели'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'get_students_count')
    list_filter = ('subject',)
    search_fields = ('name', 'subject')
    
    def get_students_count(self, obj):
        return obj.students.count()
    get_students_count.short_description = 'Количество учеников'
