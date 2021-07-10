from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Editor
from .forms import editorform
# Create your views here.
def home(request):
    form = editorform()
    return render(request,'home.html',{'form':form})