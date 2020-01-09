"""vasuproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin 
from django.conf.urls import url,include



from django.urls import path

#from . views import Home, Hellow,Empview
#from . import views as nk 
from . import views 

app_name='vasuapp'
urlpatterns = [
   # url(r'^admin/', admin.site.urls),
    path('', views.Home),
    path('tlogin/',views.tlogin,name='tlogin'),
    #path('',views.ibmcs90Home,name='ibmcs90home'),
    path('main/',views.ibmcs90Home,name='ibmcs90home.html'),
    path('budgetarea/', views.getAppNames,name='budgetarea'),
    path('budareaemp/', views.getEmpAppwise,name='budareaemp'),
    path('enoename/', views.EnoEname,name='EnoEname'),
 #   path('nkang/', views.nkang,name='nkang'),
    path('srch/', views.SrchView,name='srch'),
    path('Empview/', views.Empview,name='Empview'),
    path('index/', views.index,name='index'),
    path('cs90/', views.ICS90Empview,name='cs90'),
    path('dmretrieve/', views.getdmnames,name='dmretrieve'),
    path('myredirect/', views.myredirect,name='myredirect'),
#   path('cs90/<int:zt>', views.CS90Empview,name='CS90Empview'),
#    path('cs90/', views.CS90Empview,name='cs90'),
    
    path('cs90a/', views.CS90Empview,name='cs90a'),
    path('cs90c/', views.getEmpAppwise,name='cs90c'),
    path('cs90b/', views.ICS90Empview,name='cs90b'),
]
