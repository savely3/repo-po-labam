import math as m
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
capital = 00

for i in range(months):
    capital = capital + (spend - salary)
    spend *= 1 + increase

capital = m.ceil(capital-1)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", capital)
