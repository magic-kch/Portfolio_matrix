# Кейс «Разработка алгоритма обхода матрицы по спирали, полученной по сети»

Для работы модуля необходимо установить зависимости

`pip install -r requirements.txt`

Реализована Python-библиотеку, которая осуществляет получение квадратной 
матрицы (NxN) с удалённого сервера и возвращает её пользователю в виде 
List[int]. Этот список должен содержать результат обхода полученной матрицы 
по спирали: против часовой стрелки, начиная с левого верхнего угла.

## Использование:
```
from matrix_async import main_async
...
...
URL = 'ВАШ_АДРЕС'
asynco.run(main_async(URL))
```

## Тестирование
запустить 

```pytest```
