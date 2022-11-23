import pytest
import one_hot_encoder


def test_empty_vector():
    """
    Проверяет выброс исключения при отсутствии переменных
    """
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform()


def test_vector_by_list():
    """
    Проверка боевого сценария, когда все отрабатывает хорошо.
    Кейс 1 - вектор передается в виде списка
    """
    colors = ['blue', 'red', 'blue', 'green']
    expected_transformed_colors = [
        ('blue', [0, 0, 1]),
        ('red', [0, 1, 0]),
        ('blue', [0, 0, 1]),
        ('green', [1, 0, 0])
    ]
    assert one_hot_encoder.fit_transform(colors) == expected_transformed_colors


def test_vector_by_arguments():
    """
    Проверка боевого сценария, когда все отрабатывает хорошо.
    Кейс 2 - вектор передается в виде отдельных аргументов
    """
    expected_transformed_colors = [
        ('blue', [0, 0, 1]),
        ('red', [0, 1, 0]),
        ('blue', [0, 0, 1]),
        ('green', [1, 0, 0])
    ]
    assert one_hot_encoder.fit_transform('blue', 'red', 'blue', 'green') == \
        expected_transformed_colors


def test_numeric_vector():
    """
    Проверка боевого сценария, когда все отрабатывает хорошо.
    Кейс 3 - вектор состоящий из чисел
    """
    numeric_vector = [1, 2, 3, 1]
    expected_transformed = [
        (1, [0, 0, 1]),
        (2, [0, 1, 0]),
        (3, [1, 0, 0]),
        (1, [0, 0, 1])
    ]
    assert one_hot_encoder.fit_transform(numeric_vector) ==\
        expected_transformed
