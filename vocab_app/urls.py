from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vocabulary/', views.vocabulary_list, name='vocabulary_list'),
    path('submit_write_up/', views.submit_write_up, name='submit_write_up'),
    path('view_write_ups/', views.view_write_ups, name='view_write_ups'),
    path('signup/', views.signup, name='signup'),
    path('delete_write_up/<int:write_up_id>/', views.delete_write_up, name='delete_write_up'),
    path('delete_vocab/<int:vocab_id>/', views.delete_vocab, name='delete_vocab'),
]
