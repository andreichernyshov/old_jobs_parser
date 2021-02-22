from django.contrib import admin

from .models import City
from .models import Language
from .models import Vacancy
from .models import Error
from .models import Url


admin.site.register(Error)
admin.site.register(Language)
admin.site.register(City)
admin.site.register(Vacancy)
admin.site.register(Url)
