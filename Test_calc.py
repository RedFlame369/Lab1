import unittest
from flask import Flask, render_template, request

# Функция для расчета ипотечного платежа
def calculate_mortgage(P, annual_rate, years):
    # Преобразуем годовую процентную ставку в месячную
    r = annual_rate / 100 / 12
    # Количество месяцев в кредитном периоде
    n = years * 12
    # Формула для расчета аннуитетного платежа
    M = P * r * (1 + r)**n / ((1 + r)**n - 1)
    return M

class TestMortgageCalculator(unittest.TestCase):

    def test_calculate_mortgage(self):
        # Тест 1: Проверка с известными данными
        result = calculate_mortgage(1000000, 12, 20)
        expected_result = 11010.86  # Ожидаемый результат (считаем заранее)
        self.assertAlmostEqual(result, expected_result, places=2)

        # Тест 2: Проверка с другими данными
        result = calculate_mortgage(500000, 10, 15)
        expected_result = 5373.025588540589  # Ожидаемый результат
        self.assertAlmostEqual(result, expected_result, places=2)

        # Тест 3: Проверка с низкой процентной ставкой
        result = calculate_mortgage(200000, 1, 5)
        expected_result = 3418.7494890909384  # Ожидаемый результат
        self.assertAlmostEqual(result, expected_result, places=2)

        # Тест 4: Проверка с нулевым сроком (неверный случай, но полезен для проверки)
        with self.assertRaises(ZeroDivisionError):
            calculate_mortgage(1000000, 12, 0)

if __name__ == '__main__':
    unittest.main()