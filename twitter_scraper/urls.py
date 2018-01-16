from django.conf import settings
from django.urls import path

from . import views


urlpatterns = [
    path('api/profiles/', views.twitter_profile_api, name='twitter-profiles'),
]

if 'rest_framework' in settings.INSTALLED_APPS:
    from . import views_drf
    
    urlpatterns.append(
        path('drf_api/profiles/',
            views_drf.TwitterProfilesAPIView.as_view(),
            name='drf-twitter-profiles'
        )
    )