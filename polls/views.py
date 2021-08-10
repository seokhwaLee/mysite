from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question

# Create your views here.
def index(request):
    # 1
    # return HttpResponse("Hello, world. You're at the polls index")

    # 2
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # 3
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list' : latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # 4 render이용하면 loader와 HttpResponse를 사용하지 않고도 작성 가능
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # 1
    #return HttpResponse("You're looking at question %s." % question_id)

    # 2  
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})

    # 3 get_object_or_404() : try except없이 shortcut으로 
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})


def results(request, question_id):
    return HttpResponse(response % question_id)

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        select_choice.votes += 1
        select_choice.save()

        return HttpResponseRedirect(reverse('polls:results', arg=(question_id)))