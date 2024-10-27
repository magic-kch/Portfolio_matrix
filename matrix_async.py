from typing import List
import asyncio
import requests


def url_to_text(url: str) -> str:
    """
    Принимает URL и возвращает содержимое этого URL
    """
    if not url:
        raise ValueError('Не передан URL')
    elif not url.endswith('.txt'):
        raise ValueError('URL должен содержать расширение .txt')
    elif not requests.get(url).text:
        raise ValueError('URL не содержит содержимое')
    elif requests.get(url).status_code >= 500:
        raise ValueError('Сервер недоступен')
    elif 400 <= requests.get(url).status_code <= 500:
        raise ValueError('Неверный URL')
    return requests.get(url).text


def get_matrix(text_from_url: str):
    """
    Принимает содержимое URL и возвращает матрицу
    """
    matrix = []
    for row in text_from_url.split('\n'):
        numbers = [int(num) for num in row.split() if num.isdigit()]
        if not numbers:
            continue
        matrix.append(numbers)
    return matrix


def spiral_order(matrix: list):
    """Разворачивает матрицу по спирали против часовой стрелки"""
    if not matrix:
        return []

    result = []
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, 0

    while row < rows and col < cols:
        # Вверх
        for i in range(row, rows):
            result.append(matrix[i][col])
        col += 1

        # Вправо
        for i in range(col, cols):
            result.append(matrix[rows - 1][i])
        rows -= 1

        if row < rows:
            # Вниз
            for i in range(rows - 1, row - 1, -1):
                result.append(matrix[i][cols - 1])
            cols -= 1

        if col < cols:
            # Влево
            for i in range(cols - 1, col - 1, -1):
                result.append(matrix[row][i])
            row += 1

    return result


def main(url: str) -> List[int]:
    """Обычное выполнение кода"""
    text = url_to_text(url)
    matrix = get_matrix(text)
    flat_matrix = spiral_order(matrix)
    return flat_matrix


async def main_async(url: str) -> List[int]:
    """Асинхронное выполнение кода"""
    text = url_to_text(url)
    matrix = get_matrix(text)
    flat_matrix = spiral_order(matrix)
    return flat_matrix
