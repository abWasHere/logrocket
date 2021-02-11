from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "pk",
            "name",
            "email",
            "document",
            "phone",
            "registrationDate",
        )


"""
Serializers allow complex data such as
querysets and model instances to be converted
to native Python datatypes that can then be
easily rendered into JSON.
"""
