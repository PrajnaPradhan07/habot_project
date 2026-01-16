from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    #Add unique validator for email
    email= serializers.EmailField(
        validators=[UniqueValidator(queryset=Employee.objects.all())]
    )
    class Meta:
        model = Employee
        fields = '__all__'

    #validate name is not empty
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("name cannot be empty")
        return value

    #validate email is unique
    def validate_email(self,value):
        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("email must be unique")
        return value