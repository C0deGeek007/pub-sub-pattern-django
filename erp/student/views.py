from pickle import TRUE
from rest_framework.decorators import api_view
from rest_framework.response import Response
from student.models import Student
from student.serializers import StudentSerializer


@api_view(['GET'])
def getAllStudents(request):
    qset=Student.objects.all()
    serialiser=StudentSerializer(qset,many=True)
    return Response(serialiser.data)