from django.urls import path
from .views import get_recommendations  # Import the view function

urlpatterns = [
    path('recommendations/<int:user_id>/', get_recommendations, name='get_recommendations'),
]
