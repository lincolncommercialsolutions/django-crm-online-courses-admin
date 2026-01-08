from django.contrib import admin
from .models import Customer, Interaction, Course, Lesson, Question, Choice, Submission, Instructor, Learner
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'channel', 'direction', 'interaction_date')
    list_filter = ('channel', 'direction', 'interaction_date')
    search_fields = ('customer__name', 'summary')


# Online Course Admin
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'course', 'lesson', 'grade')
    list_filter = ('course', 'lesson')
    search_fields = ('question_text',)
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    search_fields = ('title', 'content')
    inlines = [QuestionInline]


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    search_fields = ('name', 'description')
    inlines = [QuestionInline]


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_time', 'total_learners')
    list_filter = ('full_time',)


@admin.register(Learner)
class LearnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'occupation')
    search_fields = ('user__username', 'occupation')

admin.site.register(Course, CourseAdmin)
admin.site.register(Choice)

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'submit_time')
    list_filter = ('course', 'submit_time')
    search_fields = ('user__username',)


# Register the models with their admin classes
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
