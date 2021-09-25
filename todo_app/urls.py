from django.contrib import admin
from django.urls import path,include

from.views import *

urlpatterns = [
    path('',index,name='index'),
    path('create/',create_todo,name='create'),
    path('delete-todo/<int:id>',delete_todo,name='todosil'),
    path('yes-finish/<int:id>',yes_finish,name='yesfinish'),
    path('no-finish/<int:id>',no_finish,name='nofinish'),
    path('update/<int:id>',update_doto,name='update'),
    path('login/',giris,name='login'),
    path('register/',qeydiyyat,name='register'),
    path('cixis/',cikis,name='cixis'),
]
