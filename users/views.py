from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, Http404
from django.contrib.auth.models import User
from .models import Records, Comments, PhotoAlbom
from django.core.context_processors import csrf
from .forms import CommentForm, CommentsForm, UploadFileForm
from usmessages.views import formessage
import datetime

def index(request, user_id):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:
        if str(user_id) == str(auth.get_user(request).id):
            args = {}
            args.update(csrf(request))
            args['username'] = auth.get_user(request).username
            args['records'] = Records.objects.all().order_by('-id')
            args['comments'] = Comments.objects.all().order_by('-id')
            args['id'] = auth.get_user(request).id
            args['form'] = CommentForm
            args['comment'] = CommentsForm
            args['phal'] = UploadFileForm
            args['photos'] = PhotoAlbom.objects.all()
            args['idava'] = int(forphoto(request, user_id))
            args['user_id'] = int(user_id)
            args['first_name'] = auth.get_user(request).first_name
            args['last_name'] = auth.get_user(request).last_name
            args['see'] = formessage(request)
            return render_to_response('users.html', args)
        else:
            args = {}
            args.update(csrf(request))
            args['username'] = auth.get_user(request).username
            args['records'] = Records.objects.all().order_by('-id')
            args['comments'] = Comments.objects.all().order_by('-id')
            args['id'] = auth.get_user(request).id
            args['form'] = CommentForm
            args['comment'] = CommentsForm
            args['photos'] = PhotoAlbom.objects.all()
            args['idava'] = int(avaphoto(user_id))
            args['user_id'] = int(user_id)
            args['first_name'] = User.objects.get(pk=user_id).first_name
            args['last_name'] = User.objects.get(pk=user_id).last_name
            args['see'] = formessage(request)
            return render_to_response('users.html', args)

def forphoto(request, user_id):
    idphoto = 0
    if auth.get_user(request).id == int(user_id):
        for po in PhotoAlbom.objects.all():
            if po.abpho_user_id == int(user_id):
                if po.abpho_user_photo_ava == 1:
                    idphoto = po.id
    return idphoto

def avaphoto(user_id):
    idphoto = 0
    for po in PhotoAlbom.objects.all():
        if po.abpho_user_id == int(user_id):
            if po.abpho_user_photo_ava == 1:
                idphoto = po.id
    return idphoto




def allusers(request):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:
        args = {}
        args.update(csrf(request))
        args['see'] = formessage(request)
        args['username'] = auth.get_user(request).username
        args['records'] = User.objects.all()
        args['id'] = auth.get_user(request).id
        return render_to_response('all_users.html', args)

def albompho(request):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                alpho = PhotoAlbom(abpho_user_id=auth.get_user(request).id,
                                   abpho_user_albom_id=0)
                alpho.abpho_user_photo_ava = 1
                alpho.abpho_user_photo = request.FILES['file']
                alpho.abpho_user_photo_date = "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())

                alpho.save()
                return redirect("/id%s" % auth.get_user(request).id)

        return render()

def delphoto(request, id_f):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:
        PhotoAlbom.objects.get(id=id_f).abpho_user_photo.delete()
        PhotoAlbom.objects.get(id=id_f).delete()
        return redirect("/id%s" % auth.get_user(request).id)

def bdrecords(request, user_id):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:
        if request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                rec = form.save(commit=False)
                rec.records_user_first = auth.get_user(request).first_name
                rec.records_user_last = auth.get_user(request).last_name
                rec.records_inuser_id = auth.get_user(request).id
                rec.records_user_id = user_id
                rec.records_date = "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
                form.save()
        return redirect("/id%s" % user_id)

def addcomment(request, user_id, rec_id):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:
        if request.POST:
            form = CommentsForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.comments_records_id = rec_id
                comment.comments_users_id = auth.get_user(request).id
                comment.comments_users_first = auth.get_user(request).first_name
                comment.comments_users_last = auth.get_user(request).last_name
                comment.comments_users_date = "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
                form.save()
        return redirect("/id%s" % user_id)

def addrepost(request, rec_id):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:
        inrepost = Records.objects.get(id=rec_id)
        print(inrepost.records_user_first)
        outrepost = Records(records_inuser_id=inrepost.records_inuser_id,
                records_user_first=inrepost.records_user_first,
                records_user_last=inrepost.records_user_last,
                records_text=inrepost.records_text,
                records_date=inrepost.records_date,
                repost_repost_user_id = auth.get_user(request).id,
                repost_repost_first = auth.get_user(request).first_name,
                repost_repost_last = auth.get_user(request).last_name,
                repost_repost_date = "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
                )

        outrepost.save()
        return redirect("/id%s" % outrepost.records_inuser_id)

def delpost(request, pol_id):
    Records.objects.get(id=pol_id).delete()
    return redirect("/id%s" % auth.get_user(request).id)

def addlike(request, like_id):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:
        try:
            adlike = Records.objects.get(id=like_id)
            print(adlike.records_likes_id)
            if str(auth.get_user(request).id) not in adlike.records_likes_id:
                adlike.records_likes += 1
                adlike.records_likes_id += " " + str(auth.get_user(request).id)
                adlike.save()
                print(adlike.records_likes_id)
        except ObjectDoesNotExist:
            raise Http404
        return redirect("/id%s" % adlike.records_user_id)

def addlikecom(request, like_id, user_id):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:
        try:
            adlike = Comments.objects.get(id=like_id)
            if str(auth.get_user(request).id) not in adlike.comments_users_like_id:
                adlike.comments_users_like += 1
                adlike.comments_users_like_id += " " + str(auth.get_user(request).id)
                adlike.save()
        except ObjectDoesNotExist:
            raise Http404
        return redirect("/id%s" % user_id)

def addlikere(request, like_id):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:
        try:
            adlike = Records.objects.get(id=like_id)
            print(adlike.repost_repost_likes_id)
            if str(auth.get_user(request).id) not in adlike.repost_repost_likes_id:
                adlike.repost_repost_likes += 1
                adlike.repost_repost_likes_id += " " + str(auth.get_user(request).id)
                adlike.save()
                print(adlike.repost_repost_likes_id)
        except ObjectDoesNotExist:
            raise Http404
        return redirect("/id%s" % adlike.repost_repost_user_id)

def killlike(request, like_id):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:
        try:
            adlike = Records.objects.get(id=like_id)
            print(adlike.records_likes_id)
            if str(auth.get_user(request).id) in adlike.records_likes_id:
                adlike.records_likes -= 1
                adlike.records_likes_id = adlike.records_likes_id.replace(" " + str(auth.get_user(request).id), '')
                adlike.save()
                print(adlike.records_likes_id)
        except ObjectDoesNotExist:
            raise Http404
        return redirect("/id%s" % adlike.records_user_id)

def killlikecom(request, like_id, user_id):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:
        try:
            adlike = Comments.objects.get(id=like_id)
            if str(auth.get_user(request).id) in adlike.comments_users_like_id:
                adlike.comments_users_like -= 1
                adlike.comments_users_like_id = adlike.comments_users_like_id.replace(" " + str(auth.get_user(request).id), '')
                adlike.save()
        except ObjectDoesNotExist:
            raise Http404
        return redirect("/id%s" % user_id)

def killlikere(request, like_id):
    if auth.get_user(request).id == None:
        return redirect('/')
    else:
        try:
            adlike = Records.objects.get(id=like_id)
            print(adlike.repost_repost_likes_id)
            if str(auth.get_user(request).id) in adlike.repost_repost_likes_id:
                adlike.repost_repost_likes -= 1
                adlike.repost_repost_likes_id = adlike.repost_repost_likes_id.replace(" "+str(auth.get_user(request).id), '')
                adlike.save()
                print(adlike.repost_repost_likes_id)
        except ObjectDoesNotExist:
            raise Http404
        return redirect("/id%s" % adlike.repost_repost_user_id)