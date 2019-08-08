from django.conf.urls import url, include


# Mystore apps urls
urlpatterns = [
    url(r'^', include('store.catalog.urls')),
    url(r'^accounts/', include('store.accounts.urls')),
    url(r'^pages/', include('store.pages.urls'))    
]
