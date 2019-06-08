from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from exam.models import StudentInfo,Question,ScoreInfo,PaperInfo,Course
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from random import *
import json


def Register(request):
    return render_to_response('exam/register.html')

def login(request):

    return render(request,'exam/login.html')

def index(request):
    name=json.loads(request.COOKIES.get('username'))
    return render(request,'exam/index.html',{'username':name})

def yuwen(request):
    name=json.loads(request.COOKIES.get('username'))
    question = Question.objects.filter(course=2)
    list=[]
    for i in range(2):
        if i==1:
            temp=choice(question)
            if temp==list[0]:
                temp = choice(question)
                list.append(temp)
            else:
                list.append(temp)
        else:
            list.append(choice(question))
    return render(request,'exam/yuwen.html',{'username':name,'question':list})
def shuxue(request):
    name=json.loads(request.COOKIES.get('username'))
    question = Question.objects.filter(course=1)
    list = []
    for i in range(2):
        if i == 1:
            temp = choice(question)
            if temp == list[0]:
                temp = choice(question)
                list.append(temp)
            else:
                list.append(temp)
        else:
            list.append(choice(question))
    return render(request, 'exam/shuxue.html', {'username': name, 'question': list})
@csrf_exempt
def Register1(request):

    user=StudentInfo()

    user.account=request.POST['Account1']
    user.Addr=request.POST['Address1']
    user.name=request.POST['Name1']
    user.Email=request.POST['Email1']
    user.password=request.POST['Password1']
    user.Sex=request.POST['Sex1']
    user.Tel=request.POST['Tel1']
    user.save()


    return render(request,'exam/login.html')

def Login(request):
    user = StudentInfo()
    user.account = request.POST['Account1']
    user.password = request.POST['Password1']

    user1=StudentInfo.objects.get(account=user.account)
    u = json.dumps(user1.name)

    if user1:
        if user.password==user1.password:
            response=render(request,'exam/index.html',{'username':user1.name})
            response.set_cookie('username',u)

            return response
        else:
            return render(request,'exam/login.html')
    else:
        return render(request,'exam/login.html')


# response= render_to_response('xxxx.html', {})
#       response.set_cookie('my_cookie','cookie value')
#       return response

def get_score(request):

    all_score = ScoreInfo.objects.all()
    name = json.loads(request.COOKIES.get('username'))

    return render(request, 'exam/score.html',
                  {
                      'all_score':all_score ,
                      'username': name,

                  })

def get_studentinfo(request):
    name = json.loads(request.COOKIES.get('username'))
    stu=StudentInfo.objects.get(name=name)
    return render(request,'exam/studentinfo.html',
                  {
                      'stuinfo':stu,
                      'username': name
                   })

def correcting(request):
    id_list=request.POST.getlist('ID')
    score=0
    cou1=0
    for i in id_list:
        ques=Question.objects.get(id=i)
        cou1=ques.course
        ans=request.POST[i]
        if ans==ques.answerR:
            score=score+50
    print(score)
    name1 = json.loads(request.COOKIES.get('username'))
    stu=StudentInfo.objects.get(name=name1)
    paper=PaperInfo.objects.all()[0]
    grade=ScoreInfo()
    grade.Score=score
    grade.Student=stu
    grade.course=cou1
    grade.Spaperinfo=paper
    grade.save()

    if id_list:
        return render(request,'exam/index.html')
    else:
        return render(request,'exam/register.html')














