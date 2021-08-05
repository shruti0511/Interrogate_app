from quora.forms import addAnswer
from authentication.views import topics
from django.http import response
from django.contrib import messages
from django.http.response import HttpResponse
from quora.models import Answer, Question, quoraTopic
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls.conf import include
from authentication.models import Profile
from django.shortcuts import redirect, render
from django.db.models import Q

# Create your views here.

def home(request):
    context = {}
    allQue = Question.objects.filter(status = 1).order_by('-timestamp')
    myTopics = Profile.objects.get(user = request.user).topics.all()
    context = {'allQuestions':allQue, 'myTopics': myTopics}
    return render(request,'home.html',context)

def addQuestion(request):
    if (request.method == "POST"):
        if(request.POST['question'] == ''):
            messages.error(request,'Please enter quetion!')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            queTopics = request.POST.getlist('queTopics')
            question = Question(
                question = request.POST.get('question'),
                user = request.user,
            )
            question.save()
            for i in queTopics:question.queTopics.add(i)
            messages.success(request,"your question has been asked successfully!")   
            return redirect(request.META.get('HTTP_REFERER'))

def questionDetail(request,sno):
    que = Question.objects.filter(sno=sno).get()
    print(que.question)
    context = {'que': que }
    return render(request,'questionDetails.html',context) 


def addAnswers(request):
    context ={}
    if request.method == "POST":
        if request.POST.get('answer') == '':
            messages.error(request,'Please enter answer!')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            queSno = request.POST.get('queSno')
            answer = Answer.objects.create(
                answer=request.POST.get('answer'),
                user=request.user,
                question = Question.objects.get(sno=queSno))
            answer.save()
            que = Question.objects.get(sno= queSno)
            que.status = True
            que.save()
            messages.success(request,'Your answer added successfully!!!')
            return redirect(request.META.get('HTTP_REFERER'))
                     
    else:
        que = Question.objects.filter(status = 0)
        context = {'othersQuestions' : que}
        return render(request,'addAnswers.html',context) 

def updateTopics(request):
    checked = request.POST.getlist('topics')
    checked = list(map(int, checked))
    profile = Profile.objects.get(user = request.user)
    profile.topics.clear()
    for i in checked:
        profile.topics.add(i)
    messages.success(request,'Your topics changed successfully!!!')
    return redirect(request.META.get('HTTP_REFERER'))

def search(request):
     if request.method == 'GET':
        search = request.GET.get('search')
        questions = Question.objects.filter( Q(question__icontains=search) | Q(queTopics__topic__icontains=search) | Q(user__username__icontains = search))
        context = {'searchQuestions' : questions}
        return render(request,'search.html',context)