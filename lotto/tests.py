from django.test import TestCase
from lotto.models import GuessNumbers
# Create your tests here.

class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected numbers')
        g.generate()

        print(g.update_date)
        print(g.lottos)# g.lottos #6개씩 5set 총 30개의 숫자 리스트 str

        self.assertTrue(len(g.lottos) >20)
