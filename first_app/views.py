from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def add_number(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']
    add = int(num1) + int(num2)
    print(add)
    return render(request, 'add_num.html', {'answer': add})