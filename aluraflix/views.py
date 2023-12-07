from rest_framework import viewsets, filters
from aluraflix.serializers import ProgramaSerializer
from aluraflix.models import Programa
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    # print(str(queryset.query))
    serializer_class = ProgramaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo']
    filterset_fields = ['tipo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class GetAllProgramas(APIView):

    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        programas = Programa.objects.all()
        serializer = ProgramaSerializer(programas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class PostProgramasApi(APIView):


    def post(self, request, *args, **kwargs):
        serializer = ProgramaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)