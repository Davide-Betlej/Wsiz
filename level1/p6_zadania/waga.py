import unittest
from typing import List

"""
Podana jest lista zabytkowych monet, każda oznaczona jedynie ich wagą. 
Monety trzeba podzielić na dwie grupy o równej (łącznej) wadze. Ocenić, czy da się to zrobić...
- wersja 1, prosta: poprzez wyznaczenie pozycji w liście tak, że elementy 
    na lewo od tej pozycji wchodzą do grupy1, a na prawo od niej (włącznie) do grupy 2. 
- wersja 2, trudniejsza: poprzez dowolny podział monet. 
[Uwaga: monet jest nie więcej niż 20.]
"""


def waga(coins: List[int]):
    left = coins[:-1]           # Bierze wszystkie elementy listy z wyłączeniem ostatniego elementu
    right = [coins[-1]]         # Bierze ostatni prawy element listy
    print(left)
    print(right)
    if sum(left) == sum(right):
        return True
    else:
        return False


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(waga([1, 1, 2]), True, '')

    def test_2(self):
        self.assertEqual(waga([1, 2, 3, 2]), False, '')  # True w wersji 2

    def test_3(self):
        self.assertEqual(waga([1, 1, 1]), False, '')

    def test_4(self):
        self.assertEqual(waga([1, 1, 1, ]), False, '')

    def test_5(self):
        self.assertEqual(waga([1, 1, 1, 1, 1, 1, 6]), True, '')

    def test_6(self):
        self.assertEqual(waga([2, 2, 3, 4, 5]), False, '')  # True w wersji 2


if __name__ == '__main__':
    unittest.main()