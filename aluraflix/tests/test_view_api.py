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

        self.data = {
            "titulo": "olá",
            "tipo": "F",
            "data_lancamento": "2018-04-19"
        }
        self.client = APIClient()

        self.client = APIClient()
        self.url = reverse('all-programs')
        self.url_post = reverse('post-programs')

    def test_requisicao_get_status_ok(self):
        """Testando se a requisição tem status 200 || OK"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verificar_se_response_esta_vindo_vazio(self):
        """Testando se o response está vindo vazio"""
        response = self.client.get(self.url)
        self.assertFalse('results' in response.data)

        
    def test_veriricar_post_status_201(self):
        """Teste para verificar se status do método post é 201"""
        response = self.client.post(self.url_post, self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_verificar_se_post_esta_salvando_corretamente(self):
        """Teste para veriricar se o método post está salvando corretamente"""
        response = self.client.post(self.url_post, self.data)

        self.assertEqual(self.programas.count(), 1)


        programa = Programa.objects.get()
        serializer = ProgramaSerializer(programa)
        self.assertEqual(response.data, serializer.data)