from django.shortcuts import render,redirect
from django.views.generic import View
from task.forms import TodoCreateForm,TodoChangeForm
from task.models import Todos
# Create your views here.


class TodoCreateView(View):

    def get(self,request,*args,**kwargs):
        form=TodoCreateForm()
        return render(request,"todo_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Todos.objects.create(**form.cleaned_data)

            print("todos created")
            return render(request,"todo_add.html",{"form":form})
        else:
            return render(request,"todo_add.html",{"form":form})

class TodoListView(View):

    def get(self,request,*args,**kwargs):
        qs=Todos.objects.all()
        return render(request,"todo_list.html",{"todos":qs})
    

# url:localhost:8000/todos/{id}:1,2,3
class TodoDetailView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
      
        qs=Todos.objects.get(id=id)
        return render(request,"todo_detail.html",{"todo":qs})



# localhost:8000/todos/{id}/remove

class TodoDeleteView(View):

    def get(self,request,*args,**kwrags):
        id=kwrags.get("pk")
        Todos.objects.filter(id=id).delete()
        return redirect("todo-list")


class TodoUpdateView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Todos.objects.get(id=id)
        
        form=TodoChangeForm(instance=obj)
        return render(request,"todo_edit.html",{"form":form})
    