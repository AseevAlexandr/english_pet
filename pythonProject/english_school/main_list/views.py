from django.shortcuts import render

def main_list(request):
    return render(request, 'main_list.html')
