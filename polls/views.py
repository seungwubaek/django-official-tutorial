from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django.views import generic
from django.utils import timezone as tz

from polls.models import Choice, Question


class IndexView(generic.ListView):
    template_name: str = 'polls/index.html'
    context_object_name: str = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte = tz.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name: str = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=tz.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name: str = 'polls/results.html'


def vote(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice: Choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'you didn\'t select a choice.',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
