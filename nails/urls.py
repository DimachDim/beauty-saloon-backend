from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import nails.Urls.general
import nails.Urls.boss
import nails.Urls.master
import nails.Urls.client



urlpatterns = [

    path('api/', include(nails.Urls.general)),
    path('api/', include(nails.Urls.boss)),
    path('api/', include(nails.Urls.master)),
    path('api/', include(nails.Urls.client)),
    
]



#urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)        # Для статичных файлов