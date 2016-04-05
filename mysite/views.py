from django.shortcuts import render
from django.http import HttpResponse
from .models import View
from .forms import PostForm
# Create your views here.
def show_list(request):
    list = View.objects.all()
    
    form = PostForm( request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("message")
        instance.save()
    # if request.method == "POST":
    #     print request.POST.get("name")
    #     print request.POST.get("message")
    context = {
        'object_list':list,
        'form':form,
        }
    
    # list = print list1
    return render(request, 'mysite/index.html',context)
    #return HttpResponse(print(list.as_ul()))