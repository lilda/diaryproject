from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib import auth
from django.utils import timezone
from .models import Diary, Like
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    diaries=Diary.objects.all()
    return render(request, "home.html",{"diaries":diaries})
    
def detail(request, diary_id):
        diary = get_object_or_404(Diary, pk=diary_id);
        is_L = is_like(diary, request.user);
        return render(request, "detail.html", {"diary":diary, "is_like" : is_L});
    
def update(request, diary_id):
    diary=get_object_or_404(Diary, pk=diary_id)
    
    if not request.user.is_authenticated:
        return redirect('home')
    
    if request.method =="POST":
        diary.title=request.POST['title']
        diary.content=request.POST['content']
        diary.save()
        return redirect('home')
        
    elif request.method =="GET":
        if diary.user==request.user:
            diary=get_object_or_404(Diary, pk=diary_id)
            return render(request, "update.html", {'diary':diary})
            
        if diary.user != request.user:
            return redirect('home')

def delete(request, diary_id):
    diary=get_object_or_404(Diary, pk=diary_id)
    diary.delete()
    return redirect('home')

def create(request):
    if not request.user.is_authenticated:
         return redirect('home')
         
    if request.method =="POST":
        diary=Diary()
        diary.title=request.POST['title']
        diary.content=request.POST['content']
        diary.user=request.user
        diary.time=timezone.now()
        diary.save()
        return redirect('home')
    elif request.method =="GET":
        return render(request, "new.html")
    
    
def like(request, diary_id):
    if not request.user.is_authenticated:
         return redirect('home')
    #좋아요 표시 할 글 찾기 
    diary = get_object_or_404(Diary, id=diary_id);
    #이미 좋아요 표시했는 지 확인
    obj=Like.objects.filter(diary=diary, user=request.user)
    # 좋아요 안했으면 좋아요
    if len(obj) == 0:
        obj = Like()
        obj.diary = diary
        obj.user = request.user
        obj.save()
    # 좋아요 했으면 좋아요 취소
    else:
        obj[0].delete()
    return redirect('home')
    
    
def oldlike(request, diary_id):
    user = request.user;
    diary = get_object_or_404(Diary, id=diary_id);
    #이미누른경우
    if (is_like(diary, user)):
        like=Like.objects.filter(id=diary_id, user=user);
        like.delete();
        return redirect("detail", diary_id);
    #좋아요를 하는 과정
    like = Like();
    like.diary = diary;
    like.user = user;
    like.save();
    return redirect("detail", diary_id);

def is_like(diary, user):
    if (len(Like.objects.filter(diary=diary, user=user)) != 0):
        return True;
    return False;
        
