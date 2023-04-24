from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Touristik_hudular, Category
from .forms import ContactForm
from django.views.generic import TemplateView, ListView


# Create your views here.

def obyekt_list(request):
    obyekt_list = Touristik_hudular.chiqarish.all().filter(status=Touristik_hudular.Status.Chiqarish)
    context = {
        "obyekt_list": obyekt_list
    }
    return render(request, "obyektlar/obyekt_list.html", context=context)



def obyekt_detail(request, obyektlar ):
    obyekt_detail =get_object_or_404(Touristik_hudular, slug=obyektlar, status=Touristik_hudular.Status.Chiqarish)
    context = {
        "obyekt_detail": obyekt_detail
    }
    return render(request, "obyektlar/obyekt_detail.html", context=context)



class HududlarView(ListView):
    model = Touristik_hudular
    template_name = 'obyektlar/hudud.html'
    context_object_name = 'hududlar'

    def get_queryset(self):
        samarqand = self.model.chiqarish.all().filter(category__Nomi='Samarqand')
        return samarqand




class MehmonxonaView(ListView):
    model = Touristik_hudular
    template_name = 'obyektlar/mehmonxona.html'
    context_object_name = 'mehmonxonalar'

    def get_queryset(self):
        mehmon = self.model.chiqarish.all().filter(category__Nomi='Mehmonxona')
        return mehmon




class RestoranView(ListView):
    model = Touristik_hudular
    template_name = 'obyektlar/restoran.html'
    context_object_name = 'restoranlar '

    def get_queryset(self):
        restoran = self.model.chiqarish.all().filter(category__Nomi='Restoran')
        return restoran


# def homePageView(request):
#     categories = Category.objects.all()
#     hudud = Touristik_hudular.chiqarish.all().order_by('-yozilgan_vaqti')[:8]
#     extremal_turizm_asosiy = Touristik_hudular.chiqarish.all().filter(category__Nomi='Extremal turizm').order_by('-yozilgan_vaqti')[:1]
#     extremal_turizm = Touristik_hudular.chiqarish.all().filter(category__Nomi='Extremal turizm').order_by('-yozilgan_vaqti')[:3]
#     context = {
#         'hudud': hudud,
#         'categories': categories,
#         'extremal_turizm_asosiy': extremal_turizm_asosiy,
#         'extremal_turizm': extremal_turizm
#
#     }
#     return render(request, "obyektlar/index.html", context)

class HomePageView(ListView):
     model = Touristik_hudular
     template_name = 'obyektlar/index.html'
     context_object_name = 'Touristik_hudular'

     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['categories'] = Category.objects.all()
         context['hudud'] = Touristik_hudular.chiqarish.all().order_by('-yozilgan_vaqti')[:8]
         context['extremal_turizm_asosiy'] = Touristik_hudular.chiqarish.all().filter(category__Nomi='Extremal turizm').order_by('-yozilgan_vaqti')[:1]
         context['extremal_turizm'] = Touristik_hudular.chiqarish.all().filter(category__Nomi='Extremal turizm').order_by('-yozilgan_vaqti')[:3]
         context['ziyorat_turizm'] = Touristik_hudular.chiqarish.all().filter(category__Nomi='Ziyorat turizmi').order_by('-yozilgan_vaqti')[:3]
         context['mehmonxonalar'] = Touristik_hudular.chiqarish.all().filter(category__Nomi='Mehmonxona').order_by('-yozilgan_vaqti')
         context['restoranlar'] = Touristik_hudular.chiqarish.all().filter(category__Nomi='Restoran').order_by('-yozilgan_vaqti')
         return context

# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2>Biz bilan bog'langaningiz uchun rahmat</h2>")
#     context = {
#         "form": form
#     }
#     return render(request, 'obyektlar/contact.html', context)

class ContactPageView(TemplateView):
    template_name = 'obyektlar/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'obyektlar/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h1>Biz bila bog'langanigiz uchun rahmat</h1>")
        context = {
            'form': form
        }
        return render(request, 'obyektar/contact.html', context)

