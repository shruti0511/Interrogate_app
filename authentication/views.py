from django.contrib import messages
from django.http.response import HttpResponse
from quora.models import  Answer, Question, quoraTopic
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .forms import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

def SignupUSER(request):
    if(request.method=="GET"):
        return render(request,"signup.html",{'profileform':UserProfile()})
    else:
        #Create a user
        #First check both passwords matched
        if(request.POST['password1']==request.POST['password2']):

            #Then check proper username..1)alphabets+nums=alphanums 2)all nums not and not any special chars. 3)length not more than 15 --means only alphabets or alpha+nums valid.
            if (not request.POST['username'].isalnum() or request.POST['username'].isdecimal() or len(request.POST['username'])>15):
                return render(request, 'SignUp.html',{'profileform':UserProfile(), 'error':"Username should not contain any special characters and length must be less than 15 characters"})

            #If proper then go
            else:
                #Then See this username used by someone?
                if not User.objects.filter(username=request.POST['username']).exists():
                    print(request.POST.get('username'))
                    print(request.POST.get('password1'))
                    print(request.POST.get('email'))
                    user = User.objects.create_user(
                        username=request.POST.get('username'),
                        password=request.POST.get('password1'),
                        email=request.POST.get('email'))
                    user.first_name = request.POST.get('fname')
                    user.last_name = request.POST.get('lname')
                    user.save()
                    Profile.objects.create(
                        user = user,
                        first_name = request.POST.get('fname'),
                        last_name = request.POST.get('lname'))
                    login(request,user)

                    return redirect('topics')                        
                else:
                    print('else')
                    return render(request,'signup.html',{'profileform':UserProfile(),'error':'Username already taken'})
        else:
            return render(request,'signup.html',{'fname':'demo','profileform':UserProfile(),'error':"Passwords didn't match."})



def LoginUSER(request):
    if (request.method == 'GET'):
        if request.user.is_authenticated:
            return redirect('quoraHome')
        else:
            return render(request, 'login.html')
    else:
        user = authenticate(request,username =request.POST['UserName'],password=request.POST['PassWord']) 

        if user is None:
            return render(request, 'login.html', {'error': "Don't match username and password"})
        else:
            login(request, user)
            return redirect('quoraHome')

def LogoutUSER(request):
    if request.method == 'POST':
        logout(request)
        return redirect('LoginUSER')


@login_required
def topics(request):
    context = {}
    if request.method == "POST":
        getTopics(request)
        return redirect('quoraHome')
    else:
        allTopics = quoraTopic.objects.all()
        profile = Profile.objects.get(user = request.user)
        myTopics = profile.topics.all()      
        context = {'allTopics' : allTopics,'myTopics':myTopics}
        return render(request,'topics.html',context)

@login_required
def ProfileUSER(request):
    context ={}
    if request.method == "POST": 
        profile = Profile.objects.get(user = request.user)
        if 'des' in request.POST:
            desc = request.POST.get('description')
            profile.description = desc
            profile.save()
            messages.success(request,'description added to your profile successfully!!!')
            return redirect('ProfileUSER')
        if 'emp' in request.POST:
            employment = request.POST.get('employment')
            profile.employment = employment
            profile.save()
            messages.success(request,'employment added to your profile successfully!!!')
            return redirect('ProfileUSER')
        if 'edu' in request.POST:
            school = request.POST.get('education')
            profile.school = school
            profile.save()
            messages.success(request,'education added to your profile successfully!!!')
            return redirect('ProfileUSER')
        if 'edit' in request.POST:
            employment = request.POST.get('employment')
            school = request.POST.get('education')
            description = request.POST.get('description')
            if profile.employment == employment and profile.school == school and profile.description == description:
                return redirect('ProfileUSER')
            else:
                profile.description = description
                profile.employment = employment
                profile.school = school
                profile.save()
                messages.success(request,'Credentials updated to your profile successfully!!!')
                return redirect('ProfileUSER')
    else:
        myAnswers = Answer.objects.filter(user = request.user)
        que = Question.objects.exclude(user = request.user)
        myQue = Question.objects.filter(user = request.user)
        profile = Profile.objects.get(user = request.user)
        myTopics = profile.topics.all()
        context = {'answers':myAnswers, 'othersQuestions' : que, 'questions':myQue, 'topics' : myTopics,'profile':profile}
        return render(request,'profile.html',context)


def getTopics(request):
    checked = request.POST.getlist('topics')
    checked = list(map(int, checked))
    profile = Profile.objects.get(user = request.user)
    for i in checked:
        profile.topics.add(i)

def changeProfile(request):
    if request.method == "POST":
        profile = Profile.objects.get(user = request.user)
        profile.userImage = request.FILES["img"]
        profile.save()
        return redirect('ProfileUSER')
        
@login_required
def othersProfile(request,username):
    user = User.objects.get(username = username)
    userProfile  = Profile.objects.get(user = user)
    userAnswers = Answer.objects.filter(user = user)
    userQue = Question.objects.filter(user = user)
    userTopics = userProfile.topics.all()
    context = {'profile': userProfile, 'answers':userAnswers, 'questions': userQue, 'topics': userTopics}
    return render(request,'othersProfile.html',context)      

def deleteAns(request,sno):
    answer = Answer.objects.get(sno = sno).delete()
    messages.success(request,'Your answer has been deleted successfully!!!')
    return redirect(request.META.get('HTTP_REFERER'))

def deleteQue(request,sno):
    question = Question.objects.get(sno = sno).delete()
    messages.success(request,'Your question has been deleted successfully!!!')
    return redirect(request.META.get('HTTP_REFERER'))
    



    