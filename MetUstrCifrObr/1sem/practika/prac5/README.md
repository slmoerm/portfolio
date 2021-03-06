# Задание

Изучить метод фильтрации сигналов во временной области с использованием рекурсивной фильтрации. Осуществить моделирование работы фильтра для сигналов различных видов. В работе используется ФНЧ Баттерворта 8-ого порядка с частотой среза 500 Гц

# Результат

На основе аналогового прототипа cгенерирован нерекурсивный фильтр с указанными выше параметрами. В рамках данной работы порядок фильтра равен 256:

![Ачх фильтров](<Сравнение АЧХ фильтров.png>)

Через полученный фильтр пропущен синусоидальный сигнал со следующими частотами гармоник 171.36, 428.11, 362.33 и амплитудами гармоник 5, 3, 4 соотвественно

![График фильтрации обычного сигнала](<График фильтрации обычного сигнала.png>)

Фильтрация сигнала после добавления к нему гауссовской помехи с мат. ожиданием равным 0 и дисперсией равной 1:

![Результат фильтрации силнала с гауссовским шумом](<Результат фильтрации силнала с гауссовским шумом.png>)

Фильтрация сигнала с гармонической помехой состоящей из двух гармоник синусоидального сигнала с частотами 557 и 950 Гц и амплитудами равными 1:

![Результат фильтрации сигнала с гармоническим шумом](<Результат фильтрации сигнала с гармоническим шумом.png>)

Спектр сигнала с гауссовским шумом после фильтрации:

![Спектр сигнала с гауссовским шумом](<Спектр сигнала после фильтрации.png>)
