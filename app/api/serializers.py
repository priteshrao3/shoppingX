from rest_framework import serializers
from app.models import Customer



# Customer Table
STATE_CHOICES =(
    ('assam','Assam'),
    ('bihar', 'bihar'),
)
class Serializer(serializers.ModelSerializer):
    user = serializers.ForeignKey(User, on_delete=models.CASCADE)
    name = serializers.CharField(max_length=200)
    locality = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=200)
    zipcode = serializers.IntegerField()
    state = serializers.CharField(choices=STATE_CHOICES, max_length=200)