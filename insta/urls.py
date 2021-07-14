from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name = 'index'),
    path('profile',views.show_profile, name='profile'),
    # path('update_profile',views.update_profile, name='update_profile'),
    path('posts/',views.new_post, name='post'),
    path('search/', views.search, name='search'),
    path('comment/<id>', views.comment, name='comment'),
    path('update/<id>', views.update_profile, name='update_profile'),
    path('signup/', views.signup, name='signup'),



]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)