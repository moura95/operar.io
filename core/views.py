from operator import le
from urllib import request

from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Endereco
from core.serializers import EnderecoSerializer
from core.services import ViaCepService


class EnderecosViewSet(ModelViewSet):
    serializer_class = EnderecoSerializer

    def get_queryset(self):
        queryset = Endereco.objects.all()
        cep = self.request.query_params.get("cep")

        if cep:
            cep = ViaCepService.replace_cep_address(cep=cep)
            queryset = Endereco.objects.filter(cep=cep)

        return queryset

    def create(self, request):
        try:
            if request.data["cep"]:
                cep = request.data["cep"]
                cep_exits = Endereco.objects.filter(cep=cep)
                if cep_exits:
                    return Response(
                        {"Message": "Cep already exits"}, status=status.HTTP_200_OK
                    )

                service = ViaCepService(cep)
                data = service.get_address_info()
                error = data.get("erro")
                if error:
                    raise Exception()

                data["cep"] = ViaCepService.replace_cep_address(cep=data["cep"])
                serializer = EnderecoSerializer(data=data)

                serializer.is_valid()
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"Error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST
            )
