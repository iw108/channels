
from django.urls import include, path

import example.urls

urlpatterns = [
    path('example/', include(example.urls.urlpatterns))
]
