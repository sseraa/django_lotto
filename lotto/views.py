from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm
# Create your views here.

def index(request): #get 요청
    lottos = GuessNumbers.objects.all() #행의 모든 벨류 꺼내 던짐
    return render(request,'lotto/default.html',{'lottos':lottos}) #dic--context

def hello(request):
    return HttpResponse('<h1 style="color:red;">Hello, world! </h1>')

def post(request):# 들어오는 request 가 post or get

    if request.method== 'POST':
        form = PostForm(request.POST) #filled form
            #request.POST['name'] --으로 check 가능
        if form.is_valid():
            lotto=form.save(commit = False) #임시든 진짜든 db에 반영 끝내고 리턴(save)
            lotto.generate() #form 이 아니라, db에있는 하나의 행이 됨

            return redirect('index')
    else:
        form = PostForm() # empty form
        return render(request, "lotto/form.html", {"form": form})

def detail(request,lottokey): #int:lottokey와 반드시 일치할 필요 없음.--보통매치시킴
    # print(lottokey) #str도 받아낼 수 있음 (e.g. id..)
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request,'lotto/detail.html',{'lotto':lotto}) #하나의 행 던짐
