from rest_framework import decorators, response, status

from . import serializers, models


@decorators.api_view(["GET", ])
def hello(request):
    return response.Response({"message": "Hello World!"}, status=status.HTTP_200_OK)


@decorators.api_view(["POST", ])
def add_name(request):
    serializer = serializers.NamesSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)


@decorators.api_view(["GET"])
def all_names(request):
    serializer = serializers.NamesSerializer(models.Names.objects.all(), many=True)
    return response.Response(data=serializer.data, status=status.HTTP_200_OK)
