from django.urls import path
from .views import PredictionsListView
from . import views
urlpatterns = [
    path('', PredictionsListView.as_view() , name = "predict-home"),
    path('new/', views.predict, name ="predict-new"),
]