from django.contrib import admin
from django.urls import path , include
from home import views
admin.site.site_header="Login to Ankush's Portal"
admin.site.site_title="Welcome to Ankush's Dashboard"
admin.site.index_title="Welcome to this Portal"
urlpatterns = [
path('admin/', admin.site.urls),
path('',  views.home, name='home' ),
path('home/',views.home,name='home'),
path('about',  views.about, name='about' ),
path('contact',  views.contact, name='contact' ),
path('project',  views.project, name='project' )
]