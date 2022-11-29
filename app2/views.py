from django.shortcuts import render

# Create your views here.
def a1_hai(request):
    return render(request,'a1_hai.html')

def a1_hello(request):
    return render(request,'a1_hello.html')