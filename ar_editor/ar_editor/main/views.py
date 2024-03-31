from django.shortcuts import render, redirect
from users.models import User
from augmentedreality.models import ModelStats
from augmentedreality.forms import EditModelForm


def index(request):
    if request.user.is_authenticated:
        context = {}
        context['user_name'] = request.user.username
        context['user_status'] = request.user.email
        return render(request, 'main/index.html', context=context)
    #return render(request, 'main/unlogin.html')
    return render(request, 'main/un_login.html')


def contact(request):
    #нет такого
    return render(request, 'main/contact-us.html')


def jobs(request):
    if request.user.username == '':
        return redirect('index')

    user = User.objects.get(username=request.user.username)
    user_models = list(ModelStats.objects.filter(user=user).values())

    context = {'cards': user_models}
    context['user_name'] = request.user.username
    context['user_status'] = request.user.email
    return render(request, 'main/jobs.html', context=context)


def settings(request):
    if request.user.username == '':
        return redirect('index')

    context = {}
    context['user_name'] = request.user.username
    context['user_status'] = request.user.email
    return render(request, 'main/settings.html', context)


def buy(request):
    if request.user.username == '':
        return redirect('index')

    context = {}
    context['user_name'] = request.user.username
    context['user_status'] = request.user.email
    return render(request, 'main/buy.html', context)


def error(request):
    return render(request, 'main/error404.html')
