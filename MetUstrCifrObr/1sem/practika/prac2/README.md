# Задание

Изучить основы применения алгоритма быстрого преобразования Фурье с использованием оконной функции низкого разрешения "Гаусса" с параметром 0.5 и оконной функции высокого разрешения "синус-окно" для решения задачи цифрового спектрального анализа сигналов.

# Результат

Сгенерирован синусоидальный сигнал со следующими частотами гармоник 171.36, 173.11, 662.33 и амплитудами гармоник 5, 3, 4 соотвественно

![Обычный сигнал](<График обычного дискретизированного сигнала.png>)

Вычислен его спектр с помощью обычного преобразования фурье:

![Спектр от фурье](<Спектры обычного сигнала.png>)

Вычислен спектр с помощью окна высокого разрешения:

![Спектор окно вр](<Спектры обычного с применением оконной функции высокого разрешения.png>)

Вычислен спектр с помощью окна низкого разрешения:

![Спектр окно нр](<Спектры обычного с применением оконной функции низкого разрешения.png>)

В сгенерированный ранее сигнал добавлен Гауссовский шум с мат. ожиданием равным 0.03 и дисперсией 0.02:

![График шума](<График шума.png>)

График зашумлённого сигнала:

![График зашумлённого сигнала](<График зашумлённого дискретизированного сигнала.png>)

Вычислен его спектр с помощью обычного преобразования фурье:

![Спектр от фурье](<Спектры зашумлённого сигнала.png>)

Вычислен спектр с помощью окна высокого разрешения:

![Спектор окно вр](<Спектры зашумлённого с применением оконной функции высокого разрешения.png>)

Вычислен спектр с помощью окна низкого разрешения:

![Спектр окно нр](<Спектры зашумлённого с применением оконной функции низкого разрешения.png>)
