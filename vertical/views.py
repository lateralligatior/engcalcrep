from django.shortcuts import render

def post_list(request):
    return render(request, 'vertical/post_list.html', {})
