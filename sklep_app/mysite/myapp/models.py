from django.db import models


class klient(models.Model):
    id_klient = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    haslo = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    adres = models.CharField(max_length=45)
    kod_pocztowy = models.CharField(max_length=45)
    miasto = models.CharField(max_length=45)


class zamowienie(models.Model):
    id_zamowienie = models.IntegerField(primary_key=True)
    id_klient = models.ForeignKey(klient, on_delete=models.CASCADE)
    id_towar = models.ForeignKey(towary, on_delete=models.CASCADE)
    ilosc = models.IntegerField()
    data_zamowienia = models.DateTimeField()


class kategoria(models.Model):
    id_kategoria = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length=45)


class towary(models.Model):
    id_towar = models.IntegerField(primary_key=True)
    id_kategoria = models.ForeignKey(kategoria, on_delete=models.CASCADE)
    nazwa_towaru = models.CharField(max_length=45)
    cena_brutto = models.FloatField()
    cena_netto = models.FloatField()


class admin(models.Model):
    id_admin = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=45)
    haslo = models.CharField(max_length=45)
