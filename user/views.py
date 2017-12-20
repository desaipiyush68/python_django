
from django.http import HttpResponse
from django.shortcuts import redirect,render,get_object_or_404
from django.template import loader
from .models import Users
from .forms import UsersForm
from django.views.decorators.csrf import csrf_exempt
#from django.views import render

def index(request):
    template = loader.get_template('users/index.html')
    return HttpResponse(template.render(request))


def list(request):
    all_users = Users.objects.all()
    template = loader.get_template('users/userlist.html')
    context ={
        'all_users':all_users
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template('users/adduser.html')
    return HttpResponse(template.render(request))


@csrf_exempt
def adduser(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('/list')
        else:
            return render(request, 'users/adduser.html', {
                'form': form,
                'error_message':"You have field empty"})
            

    else:
        form = UsersForm()
        return render(request, 'adduser.html', {'form': form})
        # try:
    #     name = pk=request.POST['name']
    #     email = pk= request.POST['email']
    # except (EOFError, name.DoesNotExit)
    #     return render(request, 'adduser.html', {
    #            'form': form,
    #            'error_message':"You have field empty"})
