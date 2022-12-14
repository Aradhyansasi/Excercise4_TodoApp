from django.urls import path
from TodoApp import views


urlpatterns = [
    path('signup',views.RegisterView.as_view(), name='signup'),
    path('home',views.HomeView.as_view(),name='home'),
    path('signin',views.SignInView.as_view(), name='signin'),
    path('add',views.CreateTodoView.as_view(), name='add'),
    path('all',views.ListallTodo.as_view(), name='all'),
    path('detail/<int:id>',views.TodoDetailView.as_view(), name='detail'),
    path('edit/<int:id>',views.TodoEditView.as_view(), name='edit'),
    path('delete/<int:id>',views.TodoDeleteView.as_view(), name='delete'),
    path('signout',views.SignOutView,name='signout')

]
