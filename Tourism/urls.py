from django.urls import path
from .views import obyekt_list, obyekt_detail, ContactPageView, HomePageView, \
    HududlarView, MehmonxonaView, RestoranView

urlpatterns = [
    path('', HomePageView.as_view(), name="home_page"),
    path('obyektlar/', obyekt_list, name="hamma_obyektlar"),
    path("detals/<slug:obyektlar>/", obyekt_detail, name="obyekt_detail_page"),
    path('contact-us/', ContactPageView.as_view(), name="contact_page"),
    path('hudud/', HududlarView.as_view(), name="hudud_page"),
    path('mehmonxona/', MehmonxonaView.as_view(), name="mehmonxona_page"),
    path('restoran/', RestoranView.as_view(), name="restoran_page")
]