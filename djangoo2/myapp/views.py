from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import TextService, Requestor


def index(request):
    return render(request, 'myapp/index.html')


def detail(request, question_id):
    question = get_object_or_404(TextService, pk=question_id)
    return render(request, 'myapp/detail.html', {'question': question})

def snake(request):
    return render(request, 'myapp/snake.html')

def results(request, question_id):
    question = get_object_or_404(TextService, pk=question_id)
    return render(request, 'myapp/results.html', {'question': question})


def requestor(request, question_id):
    question = get_object_or_404(TextService, pk=question_id)
    #try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    '''except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })'''
    '''else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))'''
