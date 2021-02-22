from django.contrib import admin
from django.urls import path, include
from scrap.views import home_view
from scrap.views import list_view


urlpatterns = [
    path('', home_view, name='home'),
    path('list/', list_view, name='list'),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('admin/', admin.site.urls),
]
