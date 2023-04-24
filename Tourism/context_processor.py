from .models import Touristik_hudular, Category

def latest_news(request):
    latest_news = Touristik_hudular.chiqarish.all().order_by('-yozilgan_vaqti')
    kategoriyalar = Category.objects.all()

    context = {
        'latest_news': latest_news,
        'kategoriyalar': kategoriyalar
    }
    return context