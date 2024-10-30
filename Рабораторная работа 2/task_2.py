salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

total_deficit = 0  # Общая недостача
for month in range(months):
    if month > 0:
       spend *= (1 + increase)
    deficit = max(0, spend - salary)
    total_deficit += deficit
money_capital_needed = round(total_deficit)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital_needed}")




