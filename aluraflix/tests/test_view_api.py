from typing import Any
from django.test import TestCase
from aluraflix.views import GetAllProgramas
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class ProgramaViewTestCase(TestCase):

    def setUp(self):
        self.programas = Programa.objects.all()
        self.serializer = ProgramaSerializer(instance=self.programas)

        self.client = APIClient()
        self.url = reverse('all-programs')

    def test_requisicao_get_status_ok(self):
        """Testando se a requisição tem status 200 || OK"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verificar_se_response_esta_vindo_vazio(self):
        """Testando se o response está vindo vazio"""
        response = self.client.get(self.url)
        self.assertFalse('results' in response.data)

        
        
