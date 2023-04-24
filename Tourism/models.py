from django.urls import reverse
from django.utils import timezone
from django.db import models

class ChiqarishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Touristik_hudular.Status.Chiqarish)
# Create your models here.


class Viloyatlar(models.Model):
    hudud = models.CharField(max_length=200)

    def __str__(self):
        return self.hudud
class Category(models.Model):
    Nomi = models.CharField(max_length=200)

    def __str__(self):
        return self.Nomi

class Touristik_hudular(models.Model):
    class Status(models.TextChoices):
        Tekshirish = "TEK", "Tekshirish"
        Chiqarish = "CHQ","Chiqarish"
    Mavzu = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    Matn = models.TextField()
    Rasm = models.ImageField(upload_to='hududlar/rasmlar')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    # viloyatlar = models.ForeignKey(Viloyatlar, on_delete=models.CASCADE)
    yozilgan_vaqti = models.DateTimeField(default=timezone.now)
    yaratilgan_vaqti = models.DateTimeField(auto_now_add=True)
    yangilangan_vaqti = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,
                              choices=Status.choices,
                              default=Status.Tekshirish
                              )
    korish_soni = models.IntegerField(default=0)
    object = models.Manager()
    chiqarish = ChiqarishManager()

    class Meta:
        ordering = ["-yozilgan_vaqti"]


    def __str__(self):
        return self.Mavzu

    def get_absolute_url(self):
        return reverse("obyekt_detail_page", args=[self.slug])


class Contact(models.Model):
    ism = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    xabar = models.TextField()

    def __str__(self):
        return self.xabar
