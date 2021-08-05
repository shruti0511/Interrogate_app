from django.urls import path
from.import views
from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='quoraHome'),
    path('addQuestion/',views.addQuestion, name='addQuestion'),
    path('addAnswers/',views.addAnswers, name='addAnswers'),
    path('updateTopics/',views.updateTopics, name='updateTopics'),
    path('search/',views.search, name='search'),
    path('<int:sno>/', views.questionDetail, name='questionDetail'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

