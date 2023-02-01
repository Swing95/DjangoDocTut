"""DjangoDocTut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = {
    # path vzdycky hleat - argument (tj. treba 'whatever/', pak view, potom kwargs a potom name) path nezajimaji GET
    # a post parametry kwargs - Arbitrary keyword arguments can be passed in a dictionary to the target view. We
    # aren’t going to use this feature of Django in the tutorial.
    # name - Pojmenování adresy URL vám umožní
    # jednoznačně na ni odkazovat z jiných míst v nástroji Django, zejména ze šablon. Tato výkonná funkce vám
    # umožňuje provádět globální změny vzorů URL vašeho projektu, přičemž se dotknete pouze jediného souboru.
    path('whatever/', include('polls.urls')),
    # bude mi to fungovat i bez zaregistrovane aplikace v Settings, to potrebuju az pro moduly

    path('admin/', admin.site.urls),
}
