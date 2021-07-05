from django.contrib import admin
from .models import Question, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'date_created')

    fieldsets = [
        (None, {
            'fields': [
                'question_text'
            ],
        }),
        ('Date Information', {'fields': [
         'date_created'], 'classes': ['collapse']})
    ]

    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'vote')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

admin.site.site_header = 'Poster Admin'
admin.site.site_title = 'Poster Admin Area'
admin.site.index_title = 'Welcome to te pollster admin area'
