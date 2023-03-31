from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import  NewUserForm
from Todoapp import settings
from django.core.mail import send_mail
from .models import Tasks,Register,Login
# Create your views here.



def  mail(request):
    subject="Greetings"
    msg="Congratulations for ur success"
    to="anukalias98@gmail.com"
    res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
    if res==1:
        msg="mail sent successfully"
    else:
        msg="Mail could not sent"
    return HttpResponse(msg)

class TaskList(ListView):
    model= Tasks
    context_object_name = 'task1'
    template_name = 'tasklist.html'

class TaskCreate(CreateView):
    model=Tasks
    fields='__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskcreate.html'

class TaskUpdate(UpdateView):
    model=Tasks
    fields='__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskcreate.html'

class TaskDelete(DeleteView):
    model=Tasks
    fields='__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskdelete.html'


class TaskDetailView(DetailView):
    model=Tasks
    fields='__all__'
    success_url=reverse_lazy('task1')
    template_name = 'taskdetail.html'

def register_fun(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("login")
        messages.error(request, "Unsuccessful registration.Invalid Information")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_fun(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/task-list/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})

def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('home')


class Index(View):
    def get(self,request,*args,**kwargs):
        return render(request,'home.html')

def home(request):
    template="home.html"
    context={}
    return render(request,template,context)