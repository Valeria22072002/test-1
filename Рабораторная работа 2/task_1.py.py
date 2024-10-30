money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0 # Количество месяцев, которые можно протянуть
while money_capital + salary >= spend:
    months += 1
    money_capital += salary # Добавляем зарплату
    money_capital -= spend # Вычитаем расходы
    spend *= (1 + increase) # Увеличиваем доходы на 5%
print("Количество месяцев, которое можно протянуть без долгов:",  months)