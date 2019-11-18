from django.contrib import admin



from .models import klient
admin.site.register(klient)

from .models import kategoria
admin.site.register(kategoria)

from .models import towar
admin.site.register(towar)

from .models import zamowienie
admin.site.register(zamowienie)

from .models import uzytownik
admin.site.register(uzytownik)