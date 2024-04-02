from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Carro
from .models import UserBase
from .serializers import CarroSerializer
from .serializers import UserSerializer


class CarroViewSets(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserViewSets(ModelViewSet):
    queryset = UserBase.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(['get'], False)
    def list_favorites(self, request):
        user = UserBase.objects.get(id=request.user.id)

        carros = CarroSerializer(user.favorites, many=True)
        return Response(carros.data)

    @action(['post'], False)
    def add_favorites(self, request):
        carro_id = request.data.get('id', None)

        if not carro_id:
            raise APIException({'id': 'Não foi fornecido o id do carro.'})

        carro = get_object_or_404(Carro, id=carro_id)

        user = UserBase.objects.get(id=request.user.id)
        user.favorites.add(carro)
        user.save()

        carros = CarroSerializer(user.favorites, many=True)

        return Response(carros.data)
