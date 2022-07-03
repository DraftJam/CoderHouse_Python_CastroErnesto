from django.urls import path

#from . import views
#from django.contrib.auth.views import LogoutView
from .views import AddPostView, Lista, Detalle, UpdatePostView, DeletePostView, AddCommentView

urlpatterns = [
    path ('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('lista/', Lista.as_view(), name = 'lista'),
    path('detalle/<int:pk>', Detalle.as_view(), name = 'detalle'),
    path('detalle/edit/<int:pk>', UpdatePostView.as_view(), name = 'update_post'),
    path('detalle/<int:pk>/remove', DeletePostView.as_view(), name = 'delete_post'),
    path ('article/<int:pk>/comment', AddCommentView.as_view(), name = 'add_comment')
    
]