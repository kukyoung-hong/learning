from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("POST data:", request.POST)  # 제출된 데이터 확인
        if form.is_valid():
            print("Form is valid, saving user...")
            user = form.save()
            user.email = request.POST.get('email')  # email 추가
            user.save()
            return redirect('accounts:login')
        else:
            print("Form errors", form.errors)
    else:
        form = UserCreationForm()  # 빈 폼 생성 (GET 요청용)
    return render(request,'accounts/signup.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # 로그인 세션 시작
                return redirect('myapp:home')  # 홈페이지로 리다이렉트
            else:
                messages.error(request, '아이디 또는 비밀번호가 잘못되었습니다.')
    else:
        form = AuthenticationForm()  # 빈 폼 생성 (GET 요청용)
    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('myapp:home')