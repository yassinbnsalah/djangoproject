"""mini_projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from main import views 
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_page , name="home"),
    path('', views.home_utilisateur , name="home_utlisateur"),
    path('createFormation/' , views.create_formation , name="create_formation"), 
    path('updateFormation/<str:pk>', views.update_formation , name="update_formation") ,
    path('createcategory/' , views.create_category , name="create_category"),
    path('deleteformation/<str:pk>', views.delete_formation , name="delete_formation") ,
    path('details_formation/<str:pk>' , views.details_formation , name= "details_formation"),
    path('liste_par_category/<str:pk>', views.lister_parcat , name ="liste_category"),
    path('recherche_formation/' , views.search_formation , name="rechercher_formation"),
    path('detail_formation/<str:pk>' , views.detail_formation , name="detail_formation" ),
    path('login/' , views.loginpage , name="login"),
    path('logout/' , views.logoutpage , name="logout"),
    path('registration/' , views.registration , name="register")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
