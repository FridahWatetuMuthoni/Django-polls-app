from polls.models import Question
from django.shortcuts import redirect, render
from .models import Choice, Question

# Create your views here.


def home(request):
    return render(request, 'home.html')


def polls(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'polls.html', context)


def vote(request, pk):
    question = Question.objects.get(id=pk)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error': 'You didnt select a choice'
        }
        return render(request, 'vote.html', context)
    else:
        selected_choice.vote += 1
        selected_choice
        selected_choice.save()
        return redirect('polls')


def results(request, pk):
    question = Question.objects.get(id=pk)
    context = {
        'question': question
    }
    return render(request, 'results.html', context)


def latest(request):
    questions = Question.objects.order_by('-date_created')[:5]
    context = {
        'questions': questions
    }
    return render(request, 'latest.html', context)
