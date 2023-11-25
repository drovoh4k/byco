from django.urls import path
from .views import *

app_name = 'polls'

urlpatterns = [
    path('v1/questions', Question_APIView.as_view())
]
