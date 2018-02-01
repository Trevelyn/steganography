
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='userauth/login/', permanent=True)),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS

    url(r'^admin/', admin.site.urls),
    url(r'^index/', include('main.urls',namespace='index')),
    
    url(r'^userauth/', include("RegAndLogin.urls", namespace='userauth')),
    #url(r'^logout/$', auth_views.logout,name='logout'),

    ]
