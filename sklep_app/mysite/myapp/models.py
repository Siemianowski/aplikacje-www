from django.db import models
from django.db.models import ForeignKey


class klient(models.Model):
    id_klient = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    haslo = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    adres = models.CharField(max_length=45)
    kod_pocztowy = models.CharField(max_length=45)
    miasto = models.CharField(max_length=45)

class kategoria(models.Model):
    id_kategoria = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length=45)


class towar(models.Model):
    id_towar = models.IntegerField(primary_key=True)
    id_kategoria = models.ForeignKey(kategoria, on_delete=models.PROTECT)
    nazwa_towaru = models.CharField(max_length=45)
    cena_brutto = models.FloatField(default=0)
    cena_netto = models.FloatField(default=0)


class zamowienie(models.Model):
    id_zamowienie = models.IntegerField(primary_key=True)
    id_towar = models.ForeignKey(towar, on_delete=models.PROTECT)
    id_klient = models.ForeignKey(klient, on_delete=models.PROTECT)
    ilosc = models.IntegerField(default=0)
    data_zamowienia = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return "%i " % self.ilosc





class uzytownik(models.Model):
    id_admin = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=45)
    haslo = models.CharField(max_length=45)
