from django.shortcuts import render
from rest_framework import generics
from .models import teachers
from .models import empploys
from .models import students
from .serializers import techserialisers
from.serializers import empserialisers
from .serializers import stuserialisers

class studel(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=stuserialisers
    queryset=students.objects.all()
class stulist(generics.ListCreateAPIView):
     serializer_class=stuserialisers
     queryset=students.objects.all()
     
class techlist(generics.ListCreateAPIView):
    serializer_class=techserialisers
    queryset=teachers.objects.all()
class techdel(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=techserialisers
    queryset=teachers.objects.all()
class emplist(generics.ListCreateAPIView):
    serializer_class=empserialisers
    queryset=empploys.objects.all()
class empchdel(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=empserialisers
    queryset=empploys.objects.all()
    
    
    