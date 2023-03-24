from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegisterForm,LoginForm
from Todoapp import settings
from django.core.mail import send_mail
from .models import Tasks,Register,Login
# Create your views here.



def mail(request):
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

#
# def register_fun(request):
#     register=Register.objects.all()
#     form=RegisterForm()
#
#     if request.method=='POST':
#         form =RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/login/')
#     context={'register':register,'form':form}
#     return render(request,'register.html',context)

#
# def login_fun(request):
#     login=Login.objects.all()
#     form=LoginForm()
#
#     if request.method=='POST':
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/task-list/')
#     context={'login':login,'form':form}
#     return render(request,'login.html',context)

# def home(request):
#     template="home.html"
#     context={}
#     return render(request,template,context)
# def register_fun(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']
#
#         myuser = User.objects.create_user(username, email, pass1)
#
#         myuser.save()
#
#         return redirect('login')
#
#     return render(request, 'register.html')
#
#
# def login_fun(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         pass1 = request.POST['pass1']
#
#         user = authenticate(username=username, password=pass1)
#
#         if user is not None:
#             login(request, user)
#             fname = user.username
#             return render(request, 'base.html', {'fname': fname})
#
#         else:
#             return redirect('login')
#
#     return render(request, 'login.html')
#
# def logout(request):
#     logout(request)
#     messages.success(request, 'Logged out Successfully!')
#     return redirect('login')
def register_fun(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})
def login_fun(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('/task-list/')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
class Index(View):
    def get(self,request,*args,**kwargs):
        return render(request,'home.html')
def home(request):
    template="home.html"
    context={}
    return render(request,template,context)