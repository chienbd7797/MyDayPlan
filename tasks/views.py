from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# View cho trang chủ (hiển thị sau khi đăng nhập)
def home(request):
    return render(request, 'tasks/home.html')

# View cho trang đăng nhập và đăng ký
def auth_page(request):

    if request.method == 'POST':
        # Xử lý đăng nhập
        if 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                # Đăng nhập người dùng
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')  # Chuyển hướng về trang chủ sau khi đăng nhập thành công

        # Xử lý đăng ký
        elif 'register' in request.POST:
            register_form = UserCreationForm(request.POST)
            if register_form.is_valid():
                register_form.save()  # Lưu thông tin người dùng mới
                return redirect('login')  # Chuyển hướng về trang đăng nhập sau khi đăng ký thành công

    else:
        login_form = AuthenticationForm()  # Form đăng nhập
        register_form = UserCreationForm()  # Form đăng ký

    return render(request, 'tasks/auth_page.html', {
        'login_form': login_form,
        'register_form': register_form
    })
