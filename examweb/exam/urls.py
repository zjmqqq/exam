from django.urls import path

from . import views

app_name = 'exam'
urlpatterns = [
    path('',views.login),
    path('register/', views.Register),
    path('register1/', views.Register1),
    path('login/',views.login),
    path('Login/',views.Login),
    path('index/',views.index),
    path('score/',views.get_score),
    path('studentinfo/',views.get_studentinfo),
    path('yuwen/',views.yuwen),
    path('shuxue/',views.shuxue),
    # path('getyuwen/<int:article_id>',views.get_yuwen_page),
    path('correcting/',views.correcting),

]
