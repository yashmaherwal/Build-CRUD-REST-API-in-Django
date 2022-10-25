from rest_framework.serializers import ModelSerializer
from .models import nonemployee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeSerializer
        fields = ["id", "name"]
#instagram
