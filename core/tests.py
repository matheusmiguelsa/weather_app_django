from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):
    def test_home_view_with_valid_city(self):
        city = 'São Paulo'
        url = reverse('home') + f'?city={city}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.context)
        result = response.context['result']
        self.assertIn('image1', result)
        self.assertIn('image2', result)
        self.assertIn('image3', result)
        self.assertIn('region', result)
        self.assertIn('temp_now', result)
        self.assertIn('dayhour', result)
        self.assertIn('weather_now', result)

    def test_home_view_with_invalid_city(self):
        city = 'InvalidCity'
        url = reverse('home') + f'?city={city}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.context)
        result = response.context['result']
        self.assertEqual(result['region'], 'Digite uma Cidade válida')
        self.assertEqual(result['temp_now'], '')
        self.assertEqual(result['dayhour'], '')
        self.assertEqual(result['weather_now'], '')
