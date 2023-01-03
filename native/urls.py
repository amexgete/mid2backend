from django.urls import path
from.import views
urlpatterns = [
    path('student',views.stulist.as_view()),
    path('studentDel/<int:pk>',views.studel.as_view()),
     path('teacher',views.techlist.as_view()),
    path('teacherDel/<int:pk>',views.techdel.as_view()),
    path('employ',views.emplist.as_view()),
    path('employDel/<int:pk>',views.empchdel.as_view()),
    ]
