from django import http
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from disease.models import Disease, Question, UserAnswer
from disease.forms import AnswerForm


class QuizList(ListView):
    model = Disease


class QuizDetail(DetailView):
    model = Disease
    context_object_name = 'quiz'
    queryset = Disease.objects.all()

    def first_question(self):
        return self.object.question_set.all()[0]


class QuestionDetail(DetailView):
    model = Question
    context_object_name = 'question'
    queryset = Question.objects.all()

    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = AnswerForm(initial={'question': self.object})
        return context
def report(request):
    answers = UserAnswer.objects.all()
    return render(request, "disease/report.html", {"answers" : answers})

def answer_reader(request, question_pk):
    """Process submitted answer and move to next question, or finish"""
    question= Question.objects.get(pk=question_pk)
    answer = {'True': True, 'False': False}[request.POST['answer']]
    user = request.user
    UserAnswer.objects.create(question=question, user=user, answer=answer)
    if answer == question.answer:
        messages.add_message(request, messages.SUCCESS, "Yes! That one was {}.".format(question.description))


    if question.next():
        next_question = reverse("question-detail", kwargs={'pk': question.next().pk})
        return http.HttpResponseRedirect(next_question)
    else:
        
        return http.HttpResponseRedirect("diseases/report")