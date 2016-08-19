# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf

def login(request):
    if auth.get_user(request).id != None:
        return redirect('/id%s' % auth.get_user(request).id)
    else:
        args = {}
        args.update(csrf(request))
        if request.POST:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                user = User.objects.get(pk=auth.get_user(request).id)
                user.is_active = 1
                user.save()
                return redirect('/id%s' % auth.get_user(request).id)

            else:
                args['login_error'] = "Пользователь не найден"
                return render_to_response('login.html', args)

        else:
            return render_to_response('login.html', args)

def logout(request):
    user = User.objects.get(pk=auth.get_user(request).id)
    user.is_active = 0
    user.save()
    auth.logout(request)
    return redirect("/")

def register(request):
    if auth.get_user(request).id != None:
        return redirect('/id%s' % auth.get_user(request).id)
    else:
        args = {}
        args.update(csrf(request))

        if request.POST:

            newuser_form = User.objects.create_user(
                request.POST.get('login', ''),
                request.POST.get('email', ''),
                request.POST.get('password', ''))
            newuser_form.first_name = request.POST.get('first_name', '')
            newuser_form.last_name = request.POST.get('last_name', '')
            newuser_form.save()
            newuser = auth.authenticate(
                username=newuser_form.username,
                password=request.POST.get('password', ''))
            auth.login(request, newuser)
            user = User.objects.get(pk=auth.get_user(request).id)
            user.is_active = 1
            user.save()
            return redirect('/id%s' % auth.get_user(request).id)

    return render_to_response('register.html', args)