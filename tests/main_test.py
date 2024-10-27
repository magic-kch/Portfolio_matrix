from typing import List

from matrix_async import main_async, url_to_text, get_matrix, spiral_order
import requests
import asyncio


class TestMain:
    def test_main(self):
        URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
        assert asyncio.run(main_async(URL)) == [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]

    def test_url_to_text(self):
        URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
        assert requests.get(URL).text

    def test_get_matrix(self):
        URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
        result = get_matrix(url_to_text(URL))
        assert isinstance(result, List), 'Матрица должна быть списком'
        assert all(isinstance(row, List) for row in result), 'Все элементы матрицы должны быть списками'
        assert all(all(isinstance(num, int) for num in row) for row in result),\
            'Все элементы матрицы должны быть целыми числами'

    def test_spiral_order_matrix_n_n(self):
        with open('./tests/matrix6.txt', 'r') as f:
            matrix6 = get_matrix(f.read())
        assert spiral_order(matrix6) == sorted(spiral_order(matrix6)),\
            'Матрица должна быть отсортирована по спирали'

    def test_spiral_order_matrix_n_m(self):
        with open('./tests/matrix4-6.txt', 'r') as f:
            matrix46 = get_matrix(f.read())
        assert spiral_order(matrix46) == sorted(spiral_order(matrix46)),\
            'Матрица должна быть отсортирована по спирали'
