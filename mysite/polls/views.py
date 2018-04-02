from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
from django.http import Http404
from django.urls import reverse

#import thu vien de su dung template
from django.template import loader
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #dung phuong thuc de su dung template
    #template = loader.get_template('polls/index.html')
    #bien truyen vao template
    context={'latest_question_list': latest_question_list}
    return render(request,'polls/index.html',context)
    #ngoai ra co the su dung render
    #from django.shortcuts import render
 
# Create your views here.
app_name ="polls"
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:        
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id) 
    return render(request, 'polls/results.html', {'question': question})

def vote(request,question_id):
    #ham chay try giai phong loi 404 neu co
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set_get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{'question':question,'error_message':"You didn't select a choice",})
    else:
        selected_choice.vote +=1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

