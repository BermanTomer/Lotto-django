from django.urls import path
from .views import main_view
app_name= "lotto"

urlpatterns = [
	path('', main_view, name='home'),
] 
