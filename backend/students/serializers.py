from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = (
      'studentId',
      'FirstName',
      'LastName',
      'RegistrationNo',
      'Email',
      'Course'
    )