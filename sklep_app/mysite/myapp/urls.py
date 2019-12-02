from django.urls import include, path
from rest_framework.urls import url
from . import views

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    #path('', views.index, name='index'),
    path("", views.Index.as_view(), name="index"),
    path("klient/", views.Klienci.as_view(), name="klient"),
    path("zamowienie/", views.Zamowienia.as_view(), name="zamowienie"),
    path("towar/", views.Towary.as_view(), name="towar"),
    path("kategorie/", views.Kategorie.as_view(), name="kategorie"),
    path("klient/dodaj", views.Stworz_Klienta.as_view(), name="add_klient"),
    path("zamowienie/dodaj", views.Stworz_Zamowienie.as_view(), name="add_zamowienie"),
    path("towar/dodaj/", views.Stworz_Towar.as_view(), name="add_towar"),
    path("uzytkownik/dodaj", views.Stworz_Uzytkownika.as_view(), name="add_uzytkownik"),
    path("zamowienie/edytuj", views.Edytuj_Zamowienie.as_view(), name="edit_zamowienie"),
    path("klient/edytuj", views.Edytuj_Klienta.as_view(), name="edit_klient")
]