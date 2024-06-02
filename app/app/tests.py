from django.test import SimpleTestCase

# from app.calc import add
from app.calc import add


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        self.assertEqual(add(3, 2), 5)
