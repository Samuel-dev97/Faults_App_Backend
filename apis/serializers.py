from rest_framework import serializers
from faults import models

class FaultSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description'
        ) 
        model=models.Faults