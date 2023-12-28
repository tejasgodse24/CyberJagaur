from rest_framework import serializers
from security.models import *

class AttackPercentageSerializer(serializers.Serializer):
    Label = serializers.CharField()
    Percentage = serializers.FloatField()


class AccuracySQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accuracy_SQL
        fields = ['model_name', 'Accuracy_percentage']

class AccuracyPhishingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accuracy_Phishing
        fields = ['model_name', 'Accuracy_percentage']
