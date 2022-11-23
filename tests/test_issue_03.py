import unittest
import one_hot_encoder


class TestOHE(unittest.TestCase):

    def test_empty_vector(self):
        """
        Проверяет выброс исключения при отсутствии переменных
        """
        self.assertRaises(TypeError, one_hot_encoder.fit_transform)

    def test_vector_by_list(self):
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
        self.assertListEqual(
            one_hot_encoder.fit_transform(colors),
            expected_transformed_colors
        )

    def test_vector_by_arguments(self):
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
        self.assertListEqual(
            one_hot_encoder.fit_transform('blue', 'red', 'blue', 'green'),
            expected_transformed_colors
        )

    def test_numeric_vector(self):
        """
        Проверка боевого сценария, когда все отрабатывает хорошо.
        Кейс 3 - вектор состоящий из чисел
        """
        expected_transformed = [
            (1, [0, 0, 1]),
            (2, [0, 1, 0]),
            (3, [1, 0, 0]),
            (1, [0, 0, 1])
        ]
        self.assertListEqual(
            one_hot_encoder.fit_transform([1, 2, 3, 1]),
            expected_transformed
        )
