from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout as logouts
from django.contrib.auth.models import auth
from .models import *

# Create your views here.


def router(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login_page')


def home(request):
    if request.user.is_authenticated:
        trainer = Trainer.objects.all()
        df = {'trainer': trainer}
        return render(request, 'home.html', df)
    else:
        return redirect('login_page')


def add_trainer(request):
    if request.user.is_authenticated:
        learning_path_info = Learning_Path.objects.all()
        df = {'learning_path_info': learning_path_info}
        if request.method == 'POST':
            print(request.POST)
            print(
                'sdfsaklhasflkjhsaflkjhfsalkjhasdflk---------------------------------sdfb,sfbsfb')
            trainer_name = request.POST.get('trainer_name')
            adderes = request.POST.get('adderes')
            phone_no = request.POST.get('phone_no')
            phone_no_optional = request.POST.get('phone_no_optional')
            email = request.POST.get('email')
            email_optional = request.POST.get('email_optional')
            gender = request.POST.get('gender')
            trainer_international = request.POST.get(
                'trainer_international')
            trainer_pricing = request.POST.get('trainer_pricing')
            trainer_course_specialization = request.POST.get(
                'trainer_course_specialization')
            trainer_skill_set = request.POST.get('trainer_skill_set')
            trainer_enrolled_with = request.POST.get('trainer_enrolled_with')
            trainer_tier = request.POST.get('trainer_tier')
            trainer_attachment = request.FILES.getlist('trainer_attachment')

            for trainer_attachment in trainer_attachment:
                trainer_attachment = trainer_attachment

            obj = Trainer(trainer_name=trainer_name, adderes=adderes, phone_no=phone_no, phone_no_optional=phone_no_optional, email=email,
                          email_optional=email_optional, gender=gender, trainer_international=trainer_international,
                          trainer_pricing=trainer_pricing, trainer_course_specialization=trainer_course_specialization,
                          trainer_skill_set=trainer_skill_set, trainer_enrolled_with_id=trainer_enrolled_with,
                          trainer_tier=trainer_tier, trainer_attachment=trainer_attachment)

            obj.save()
            learning_path_info = Learning_Path.objects.all()
            trainer = Trainer.objects.all()

            df = {'learning_path_info': learning_path_info, 'trainer': trainer}

            return render(request, 'add_trainer.html', df)

        else:
            print('hello')
            learning_path_info = Learning_Path.objects.all()
            trainer = Trainer.objects.all()
            df = {'learning_path_info': learning_path_info, 'trainer': trainer}
            return render(request, 'add_trainer.html', df)
    else:
        html = '<!DOCTYPE html><html><head></head><body><h1> Unauthorized Access </h1></body></html>'
        return HttpResponse(html)


def trainer_info(request, trainer_id):
    if request.user.is_authenticated:
        info = Trainer.objects.get(trainer_id=trainer_id)

        df = {'info': info}
        return render(request, 'trainer_info.html', df)
    else:
        return redirect('router')


def edit_trainer(request, trainer_id):
    if request.user.is_authenticated:
        info = Trainer.objects.get(trainer_id=trainer_id)
        learning_path_info = Learning_Path.objects.all()

        df = {'info': info, 'learning_path_info': learning_path_info}
        if request.method == 'POST':
            print(request.POST)
            trainer_name = request.POST.get('trainer_name')
            adderes = request.POST.get('adderes')
            phone_no = request.POST.get('phone_no')
            phone_no_optional = request.POST.get('phone_no_optional')
            email = request.POST.get('email')
            email_optional = request.POST.get('email_optional')
            gender = request.POST.get('gender')
            trainer_international = request.POST.get('trainer_international')
            trainer_pricing = request.POST.get('trainer_pricing')
            trainer_course_specialization = request.POST.get(
                'trainer_course_specialization')
            trainer_skill_set = request.POST.get('trainer_skill_set')
            trainer_enrolled_with = request.POST.get('trainer_enrolled_with')
            trainer_tier = request.POST.get('trainer_tier')
            trainer_attachment = request.POST.get('trainer_attachment')

            info.trainer_name = trainer_name
            info.adderes = adderes
            info.phone_no = phone_no
            info.phone_no_optional = phone_no_optional
            info.email = email
            info.email_optional = email_optional
            info.gender = gender
            info.trainer_international = trainer_international
            info.trainer_pricing = trainer_pricing
            info.trainer_course_specialization = trainer_course_specialization
            info.trainer_skill_set = trainer_skill_set
            info.trainer_enrolled_with = trainer_enrolled_with
            info.trainer_tier = trainer_tier
            info.trainer_attachment = trainer_attachment
            info.save()

        return render(request, 'edit_trainer.html', df)
    else:
        return redirect('router')


# blogid = Blog.objects.get(id=blog_id)
#         result = {"x": blogid}
#         if request.method == 'POST':
#                 print(request.POST)
#                 title = request.POST.get('title')
#                 body = request.POST.get('body')
#                 status_draft = request.POST.get('status_draft')
#                 status_publish = request.POST.get('status_publish')
#                 if status_draft == 'on':
#                     status_draft = True
#                 else:
#                     status_draft = False
#                 if status_publish == 'on':
#                     status_publish = True
#                 else:
#                     status_publish = False

#                 blogid.title = title
#                 blogid.body = body
#                 blogid.status_draft = status_draft
#                 blogid.status_publish = status_publish
#                 blogid.save()
#                 context = {'blogdetail':blogid}
#                 # return render(request, 'editblog.html', context)
#                 blogdata =  Blog.objects.filter(author_instance= request.user.authorinstance)
#                 result = {"all_blogdata": blogdata}
#                 return render(request, 'author_page.html', result)


def lerning_path(request):
    learning_path = Learning_Path.objects.all()
    trainer = Trainer.objects.all()
    df = {'learning_path': learning_path, 'trainer': trainer}
    return render(request, 'add_trainer.html', df)


def add_lerning_path(request):
    trainer = Trainer.objects.all()
    df = {'trainer': trainer}
    if request.method == 'POST':
        name = request.POST.get('name')

        obj = Learning_Path(name=name)
        obj.save()

    return render(request, 'add_lerning_path.html', df)


def search_a_trainer(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        trainers = Trainer.objects.filter(trainer_name__contains=searched)

    return render(request, 'search_a_trainer.html', {'searched': searched, 'trainers': trainers})


def login_page(request):
    if request.user.is_authenticated:
        print("hello")
        return redirect('router')

    else:
        print("hello else")
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)

                return redirect('router')
            else:
                return HttpResponse("Invalid username or password")
        else:
            return render(request, 'login_page.html')


def logout(request):
    if request.user.is_authenticated:

        logouts(request)
        return redirect('router')

    else:
        return redirect('router')
