from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofrectangle/',views.surfacearea,name="areaofrectangle"),
    path('',views.surfacearea,name="areaofrectangleroot")
]