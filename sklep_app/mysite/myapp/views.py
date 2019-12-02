from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import zamowienie, kategoria, towar, klient, uzytkownik
from .serializers import zamowieniaSerializer, kategoriaSerializer, towarSerializer, klientSerializer, uzytkownikSerializer

# def index(request):
#     return HttpResponse("Hello, world. You're at the myapp index.")

class Index(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello {self.request.user}!"}, status=200)

class Klienci(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {"Klienci": klientSerializer(klient.objects.all(), many=True).data},
            status=200,
        )

class Towary(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {"Towary": towarSerializer(towar.objects.all(), many=True).data}, status=200
        )

class Zamowienia(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {"Zamowienia": zamowieniaSerializer(zamowienie.objects.all(), many=True).data}, status=200
        )

class Kategorie(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {"Kategorie": kategoriaSerializer(kategoria.objects.all(), many=True).data}, status=200
        )

class Stworz_Klienta(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = klientSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Klient stworzony"}, 200)
        else:
            return Response({"message": "Klient nie stworzony!"}, 400)

class Stworz_Zamowienie(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = zamowieniaSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Zamowienie stworzone"}, 200)
        else:
            return Response({"message": "Zamowienie nie stworzone!"}, 400)

class Stworz_Towar(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = towarSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Towar stworzony"}, 200)
        else:
            return Response({"message": "Towar nie stworzony!"}, 400)


class Edytuj_Klienta(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def patch(self, request):
        serializer = klientSerializer(
            self.request.klient, data=self.request.data, partial=True   #user
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Klient zaktualizowany"}, 200)
        else:
            return Response({"error": serializer.errors}, 400)

class Stworz_Uzytkownika(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = uzytkownikSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Uzytkownik stworzony"}, 200)
        else:
            return Response({"message": "Uzytkownik nie stworzony!"}, 400)

class Edytuj_Zamowienie(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    def patch(self, request):
        try:
            zamowienie1 = zamowienie.objects.get(name=self.request.data["id_zamowienie"])
        except Exception:
            return Response({"error": "Zamowienie nie istnieje"}, 400)

        serializer = zamowieniaSerializer(zamowienie1, data=self.request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Zamowienie zaktualizowane"}, 200)
        else:
            return Response({"error": serializer.errors}, 400)