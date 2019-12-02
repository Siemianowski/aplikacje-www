from django.contrib import admin
from django.urls import include, path
from rest_framework.urls import url
#from ..myapp.views import Index


# from ..myapp.views import (
    #Index
    #Klienci,
    # Zamowienia,
    # Towary,
    # Kategorie,
    # Stworz_Klienta,
    # Stworz_Zamowienie,
    # Stworz_Towar,
    # Stworz_Uzytkownika,
    # Edytuj_Zamowienie,
    # Edytuj_Klienta,
#)


urlpatterns = [
    #url(r'^api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include("rest_framework.urls")),
    #path("", Index.as_view(), name="index"),
    #path("klient/", Klienci.as_view(), name="klient"),
    # path("zamowienie/", Zamowienia.as_view(), name="zamowienie"),
    # path("towar/", Towary.as_view(), name="towar"),
    # path("kategorie/", Kategorie.as_view(), name="kategorie"),
    # path("klient/dodaj", Stworz_Klienta.as_view(), name="add_klient"),
    # path("zamowienie/dodaj", Stworz_Zamowienie.as_view(), name="add_zamowienie"),
    # path("towar/dodaj/", Stworz_Towar.as_view(), name="add_towar"),
    # path("uzytkownik/dodaj", Stworz_Uzytkownika.as_view(), name="add_uzytkownik"),
    # path("zamowienie/edytuj", Edytuj_Zamowienie.as_view(), name="edit_zamowienie"),
    # path("klient/edytuj", Edytuj_Klienta.as_view(), name="edit_klient")
    #path('myapp/', include('myapp.urls')) ###?????
]