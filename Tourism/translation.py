from modeltranslation.translator import register, TranslationOptions
from .models import Touristik_hudular, Category


@register(Touristik_hudular)
class HududTranslationOptions(TranslationOptions):
    fields = ('Mavzu', 'Matn')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('Nomi',)