from django.contrib import admin

# Register your models here.
from .models import Category, Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)