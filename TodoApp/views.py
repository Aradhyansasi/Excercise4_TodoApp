from django.shortcuts import render, redirect
from TodoApp.models import Todo, User
from TodoApp.forms import RegisterForm, LoginForm, TodoForm
from django.views.generic import CreateView, TemplateView, FormView, ListView, DetailView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('signin')

class HomeView(TemplateView):
    template_name = 'home.html'


class SignInView(FormView):
    model = User
    form_class = LoginForm
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print('usernaem: ',username, "password: ", password)
            user = authenticate(request, username=username, password=password)
            print("******User****: ", user)
            if not user:
                return render(request, 'login.html', {'form':form})
            login(request,user)
            return redirect('home')


class CreateTodoView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'TodoCreate.html'

    def post(self, request,*args,**kwargs):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
        else:
            return redirect('add')


class ListallTodo(ListView):
    model = Todo
    template_name = 'allTodo.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('-date')


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todoDetail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'todo'

class TodoEditView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'editTodo.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('all')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoDeleteView(View):
    def get(self,request, *args, **kwargs):
        id = kwargs.get('id')
        todo = Todo.objects.get(id=id)
        todo.delete()
        return redirect('all')


def SignOutView(request, *args, **kwargs):
    logout(request)
    return redirect('signin')