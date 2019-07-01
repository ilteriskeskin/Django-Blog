from django.shortcuts import render, HttpResponse
from .models import Blog
from .forms import ContactForm

# Create your views here.


def contact(request):
    form = ContactForm()
    return render(request, '')

def post_list(request):
    posts = Blog.objects.all()
    context = {'posts': posts, 'sayi': sayi}
    return render(request, 'blog/post-list.html', context)


def post_update(request):
    deneme = "Burada Gönderiler Güncellenecek"
    return HttpResponse(deneme)


def post_delete(request):
    ali = "Burada gönderi silinecektir"
    return HttpResponse(ali)


def post_create(requset):
    create = "<strong>Burada post oluşturulacaktır</strong>"
    return HttpResponse(create)