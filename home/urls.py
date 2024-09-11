from django.urls import path
from .views import *
from .views import recipe
from .views import delete_recipe
from .views import update_recipe
from .views import login_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", recipe, name='recipe'),
    path("delete_recipe/<id>/", delete_recipe, name='delete_recipe'),
    path("update_recipe/<id>/", update_recipe, name='update_recipe'),
    path("Login/", login_page, name='login_page'),
    path("register/",register_page, name='resister_page'),
    path("logout_page/", logout_page, name='logout_page')

]


# project/urls.py

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








