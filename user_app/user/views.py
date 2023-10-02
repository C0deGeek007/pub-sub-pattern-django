from pickle import TRUE
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.serializers import UserSerializer, permissionSerializer
from django.contrib.auth.models import User, Permission

from user.task import add, produce_permission_update_message

@api_view(['GET'])
def getAllUsers(request):
    qset=User.objects.all()
    serialiser=UserSerializer(qset,many=True)
    result =add.delay(10,20)
    return Response(serialiser.data)

@api_view(['POST'])
def createUser(request):
    serialiser=UserSerializer(data=request.data)
    serialiser.is_valid()
    if(serialiser.is_valid(raise_exception=True)):
        serialiser.save()
        return Response(serialiser.data)

# myuser.user_permissions.remove(permission, permission, ...)


@api_view(['POST'])
def updateUser(request):
    request_data = request.data
    user = User.objects.get(id=request_data.get("user"))
    permisison = Permission.objects.get(id=request_data.get("permission"))
    user.user_permissions.add(permisison)
    # user.user_permissions.remove(permisison)
    user.save()
    serializer = UserSerializer(user)
    produce_permission_update_message(serializer.data)
    user.user_permissions.remove(permisison)
    return Response(serializer.data)

@api_view(['GET'])
def getUserPermission(request):
    user = User.objects.get(id=request.GET.get("user"))
    serializer = UserSerializer(user)
    return Response(serializer.data)


# curl -X POST http://127.0.0.1:8000/updateAccount & curl -X POST http://127.0.0.1:8000/updateAccount & curl -X POST http://127.0.0.1:8000/updateAccount & curl -X POST http://127.0.0.1:8000/updateAccount & curl -X POST http://127.0.0.1:8000/updateAccount & curl -X POST http://127.0.0.1:8000/updateAccount

#sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management

# redis-cli

# permission id's 
#37

# from django.contrib.auth.models import Permission, User
# from django.contrib.contenttypes.models import ContentType
# content_type = ContentType.objects.get_for_model(User)
# permission = Permission.objects.create(
#     codename="can_take_action1",
#     name="Can take action1",
#     content_type=content_type,
# )
# print(permission)
# auth | user | Can take action1
# print(permission.id)