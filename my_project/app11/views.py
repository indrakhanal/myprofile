from django.shortcuts import render, redirect, HttpResponse
from .models import Person, Project, Gallery, Contact, Tolls, Skill
from django.contrib import messages


def home(request):
    info = Person.objects.all()
    tool = Tolls.objects.all()
    skill = Skill.objects.all()
    context = {
        'info': info,
        'tool': tool,
        'skill': skill
    }
    return render(request, 'home.html', context)


def project(request):
    p_info = Project.objects.all()
    context = {
        'p_info': p_info
    }
    return render(request, 'project.html', context)


def gallery(request):
    img = Gallery.objects.all()
    count = len(img)
    context = {
        'img': img,
        'count': count
    }
    return render(request, 'gallery.html', context)


def contact(request):
    return render(request, 'contact.html')


def send_message(request):
    if request.method == 'GET':
        return redirect('contact')
    else:
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            data = Contact(name=name, email=email, subject=subject, message=message)
            if name and email and messages is not None:
                data.save()
                messages.add_message(request, messages.SUCCESS, 'Successfully send your message')
                return redirect('contact')

            else:
                messages.add_message(request, messages.ERROR, 'all field must be filled out')
                return redirect('contact')

            # else:
            #     messages.add_message(request, messages.ERROR, 'Field should not empty')
            #     return redirect('contact')
        except:
            messages.add_message(request, messages.ERROR, 'Error on Sending please try again')
            return redirect('contact')


def complete_project(request):
    p = Project.objects.filter(p_id=1)
    p1 = Project.objects.all()
    context = {
        'p': p,
        'p1': p1
    }
    return render(request, 'project_detail.html', context)
