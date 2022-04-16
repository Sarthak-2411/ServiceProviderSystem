"""HomeServices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from otp_module import views as otp_view
from django.conf import settings
from django.conf.urls.static import static, serve

handler404 = 'home_page.views.error_404'
handler500 = 'home_page.views.error_500'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('admin_panel/',include('admin_panel.urls')),
    path('',include('home_page.urls'),name = "home"),
    
    
    path('get_otp/',otp_view.get_otp,name='get_otp'),
    path('check_otp/',otp_view.check_otp,name='check_otp'),
    path('cust_login/', include('customer_login.urls'),name = 'cust_login'),
    path('provider_register/',include('provider_login.urls'),name='prov_signup'),
    path('service_booking/',include('Booking.urls'),name='service_booking'),


    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
