from.models import students
from.models import teachers
from.models import empploys
from rest_framework import serializers
class stuserialisers(serializers.ModelSerializer):
      class Meta:
        model=students
        fields='__all__'
class techserialisers(serializers.ModelSerializer):
      class Meta:
        model=teachers
        fields='__all__'
class empserialisers(serializers.ModelSerializer):
      class Meta:
        model=empploys
        fields='__all__'


