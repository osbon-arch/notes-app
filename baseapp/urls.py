""" defines urls for baseapp"""


from django.urls import path
from . import views
app_name = 'baseapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('topics/',views.topics,name='topics'),
    path('topics/<int:topic_id>',views.topic,name='topic'),
    #page for adding anew topic
    path('new_topic',views.new_topic, name='new_topic'),
]
