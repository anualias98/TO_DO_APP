from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, TaskDetailView, home, Index
from .import views
urlpatterns=[
    path('mail/',views.mail),
    path('task-list/' ,TaskList.as_view(),name='task1'),
    path('task-create/' ,TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
    path('task-detail/<int:pk>/',TaskDetailView.as_view(),name='task-detail'),
    path('login/',views.login_fun,name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/',views.register_fun,name='Register'),
    path('',Index.as_view(),name='index'),
    path('home/',home,name="home"),
]