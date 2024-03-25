from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Student
from .serializers import StudentSerializers

# Create your views here.
class StudentView(APIView):

  # post or add data
  def post(self, request):
    data = request.data
    serializer = StudentSerializers(data=data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse('Student Added Successfully', safe=False)
    
    
    return JsonResponse('Failed to Add Student', safe=False)
  
  # get or read data
  def get_student(self, pk):
    try:
      student = Student.objects.get(studentId = pk)
      return student
    except Student.DoesNotExist:
      raise Http404
    
  def get(self, request, pk = None):
    if pk:
      data = self.get_student(pk)
      serializer = StudentSerializers(data)
    else:
      data = Student.objects.all()
      serializer = StudentSerializers(data, many=True)
    
    return Response(serializer.data)
  
  # put or update data
  def put(self, request, pk=None):
    student_to_update = Student.objects.get(studentId=pk)
    serializer = StudentSerializers(instance=student_to_update, data=request.data, partial=True)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse('Student updated Successfully', safe=False)
    return JsonResponse('Failed to Update Student')
  
  # delete data
  def delete(self, request, pk):
    student_to_delete = Student.objects.get(studentId=pk)
    student_to_delete.delete()
    return JsonResponse('Student Deleted Successfully', safe=False)