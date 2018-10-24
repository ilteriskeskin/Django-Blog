from django.shortcuts import render, HttpResponse
from .models import Blog

# Create your views here.


def post_list(request):
    posts = Blog.objects.all()
    sayi = 1
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


def sanatcilar(request, sayi):
    sanatcilar_sozluk = {
        '1': 'Tarkan',
        '2': 'Merve Özbey',
        '3': 'Norm Ender',
        '4': 'Neşet Ertaş',
        '5': 'Ali İlteriş Keskin',
        '6': 'Teoman',
        '98': 'Müslüm Gürses',
        '9': 'Selo',
        'eminem': 'deneme',
    }

    sanatci = sanatcilar_sozluk.get(sayi, "Bu id'ye ait sanatçı bulunamadı")
    return HttpResponse(sanatci)
