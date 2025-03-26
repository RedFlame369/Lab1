from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_mortgage(P, annual_rate, years):
    # Преобразуем годовую процентную ставку в месячную
    r = annual_rate / 100 / 12
    # Количество месяцев в кредитном периоде
    n = years * 12
    # Формула для расчета аннуитетного платежа
    M = P * r * (1 + r) ** n / ((1 + r) ** n - 1)
    return M


@app.route('/', methods=['GET', 'POST'])
def index():
    monthly_payment = None
    if request.method == 'POST':
        # Получаем данные из формы
        amount = float(request.form['amount'])
        rate = float(request.form['rate'])
        years = int(request.form['years'])

        # Рассчитываем ежемесячный платеж
        monthly_payment = calculate_mortgage(amount, rate, years)

    return render_template('index.html', monthly_payment=monthly_payment)


if __name__ == '__main__':
    app.run(debug=True)
