from rest_framework import serializers
import re

from .models import towar, klient, kategoria, zamowienie, uzytownik


class klientSerializer(serializers.ModelSerializer):
    class Meta:
        model = klient
        fields = ["id_klient", "login", "email", "haslo", "nazwisko", "adres", "kod_pocztowy"]

        def validate_login(self, login):
            if not login or not login.isalpha():
                raise serializers.ValidationError("Login cannot be empty field")

        def validate_email(self, email):
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if not (re.search(regex, email)):
                raise serializers.ValidationError("Wrong email format!")
            else:
                return email

        def validate_password(self, haslo):
            if len(haslo) < 8:
                raise serializers.ValidationError("Make sure your password is at lest 8 letters")
            elif re.search('[0-9]', haslo) is None:
                raise serializers.ValidationError("Make sure your password has a number in it")
            elif re.search('[A-Z]', haslo) is None:
                raise serializers.ValidationError("Make sure your password has a capital letter in it")
            else:
                return haslo

        def validate_surname(self, nazwisko):
            if not nazwisko or not nazwisko.isalpha():
                raise serializers.ValidationError("Surname cannot be empty field")
            return nazwisko.title()

        def validate_adres(self, adres):
            if not adres:
                raise serializers.ValidationError("You must type something!")
            elif len(adres) > 45:
                raise serializers.ValidationError("Your comment can only have 45 letters!")
            else:
                return adres


class kategoriaSerializer():
    class Meta:
        model = kategoria
        fields = ["id_kategoria", "nazwa"]

    def validate_content(self, nazwa):
        if not nazwa:
            raise serializers.ValidationError("You must type something!")
        elif len(nazwa) > 45:
            raise serializers.ValidationError("Your comment can only have 45 letters!")
        else:
            return nazwa


class towarSerializer(serializers.ModelSerializer):
    class Meta:
        model = towar
        fields = ["id_towar", "id_kategoria", "nazwa_towaru", "cena_brutto", "cena_netto"]

    def validate_nazwa_towaru(self, nazwa_towaru):
        if not nazwa_towaru:
            raise serializers.ValidationError("You must type something!")
        elif len(nazwa_towaru) > 45:
            raise serializers.ValidationError("Your comment can only have 45 letters!")
        else:
            return nazwa_towaru

    def validate_cena(self, cena_brutto):
        if not cena_brutto:
            raise serializers.ValidationError("You must type something!")
        return cena_brutto


class zamowieniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = zamowienie
        fields = ["id_zamowienie", "id_towar", "id_klient", "ilosc", "data_zamowienia"]


class uzytkownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = uzytownik
        fields = ["id_admin", "login", "haslo"]

        def validate_password(self, haslo):
            if len(haslo) < 8:
                raise serializers.ValidationError("Make sure your password is at lest 8 letters")
            elif re.search('[0-9]', haslo) is None:
                raise serializers.ValidationError("Make sure your password has a number in it")
            elif re.search('[A-Z]', haslo) is None:
                raise serializers.ValidationError("Make sure your password has a capital letter in it")
            else:
                return haslo

        def validate_login(self, login):
            if not login or not login.isalpha():
                raise serializers.ValidationError("Login cannot be empty field")
