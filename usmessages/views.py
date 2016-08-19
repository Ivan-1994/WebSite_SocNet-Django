from django.shortcuts import render
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from .models import UsMessages
from django.contrib.auth.models import User
from .forms import MessageUser
import datetime


def usmessages(request):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:
        args = {}
        args.update(csrf(request))
        args['id'] = auth.get_user(request).id
        args['username'] = auth.get_user(request).username
        args['mesall'] = UsMessages.objects.all().order_by('-id')
        args['idlist'] = listmessages(request)
        args['us_id'] = auth.get_user(request).id
        args['see'] = formessage(request)
        return render_to_response('messages.html', args)

def listmessages(request):
    um = UsMessages.objects.all().order_by('-id')
    inlist = []
    outlist = []
    intlist = []
    for umi in um:
        if umi.message_user_id == auth.get_user(request).id and umi.message_outuser_id not in inlist:
            if umi.message_outuser_id not in outlist:
                outlist.append(umi.message_outuser_id)
                intlist.append(umi.id)
        elif umi.message_outuser_id == auth.get_user(request).id and umi.message_user_id not in outlist:
            if umi.message_user_id not in inlist:
                inlist.append(umi.message_user_id)
                intlist.append(umi.id)
    return intlist



def usmessage(request, user_id):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:

        args = {}
        args.update(csrf(request))
        args['username'] = auth.get_user(request).username
        args['id'] = auth.get_user(request).id
        args['messageusername'] = str(User.objects.get(pk=user_id).first_name)+" "+str(User.objects.get(pk=user_id).last_name)
        args['mesall'] = UsMessages.objects.all().order_by('-id')
        args['inlist'] = inlistmessage(request, user_id)
        args['outlist'] = outlistmessage(request, user_id)
        args['form'] = MessageUser
        args['user_id'] = int(user_id)
        args['see'] = formessage(request)
        return render_to_response('message.html', args)

def inlistmessage(request, user_id):
    mes = UsMessages.objects.all().order_by('-id')
    inlist = []
    for me in mes:
        if me.message_user_id == int(user_id) and me.message_outuser_id == auth.get_user(request).id:
            me.message_see = 0
            me.save()
            inlist.append(me.id)
    return inlist

def outlistmessage(request, user_id):
    mes = UsMessages.objects.all().order_by('-id')
    outlist = []
    for me in mes:
        if me.message_user_id == auth.get_user(request).id and me.message_outuser_id == int(user_id):
            outlist.append(me.id)
    return outlist

def addmessage(request, user_id):
    if request.POST:
        form = MessageUser(request.POST)
        if form.is_valid():
            ob = form.save(commit=False)
            ob.message_user_id = auth.get_user(request).id
            ob.message_user_name = str(auth.get_user(request).first_name)+" "+str(auth.get_user(request).last_name)
            ob.message_outuser_id = user_id
            ob.message_outuser_name = str(User.objects.get(pk=user_id).first_name)+" "+str(User.objects.get(pk=user_id).last_name)
            ob.message_date = "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
            ob.message_see = 1
            form.save()
        return redirect("/message%s" % user_id)

def formessage(request):
    um = UsMessages.objects.all()
    a = 0
    for u in um:
        if u.message_outuser_id == auth.get_user(request).id:
            if u.message_see == 1:
                a += 1
    return a
