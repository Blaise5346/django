from django.shortcuts import render

# Create your views here.
from .models import Question

def display_questions(request):
    questions = Question.objects.all()
    return render(request, 'quiz_app/display_questions.html', {'questions': questions})