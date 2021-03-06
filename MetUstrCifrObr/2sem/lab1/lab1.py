# Const
N = 4024



def signal_generate(time, function):
    """ 
    Генерирует сигнал с заданными параметрами

    :time: Отсчёты сигнала
    :function: Функция по которой строиться график
    :returns: Сигнал с заданными параметрами
    """
    from numpy import log, pi, cos 

    generated_signal = eval(function)

    return generated_signal 


def interpolation_signal_plot(high_discretization_signal, high_discretization_numbers, low_discretization_signal,
                              low_discretization_numbers, interpolated_signal, interpolation_method):
    """
    Строит три графика с заданной дискретизацией

    :high_discretization_signal: Сигнал с высокой частотой дискретизации
    :high_discretization_numbers: Отсчёты сигнала с высокой частотой дискретизации
    :low_discretization_signal: Сигнал с низкой частотой дискретизации
    :low_discretization_numbers: Отсчёты сигнала с низкой частотой дискретизации
    :input_signal: Сигнал с низкой частотой дискретизации прошедший интерполяцию
    :interpolation_method: Метод интерполяции
    """
    import matplotlib.pyplot as plt
    import numpy as np

    plt.figure()
    plt.title("Интерполяция {} методом".format(interpolation_method))
    plt.xlabel('Отсчёты')
    plt.ylabel('Амплитуда')
    plt.plot(high_discretization_numbers, high_discretization_signal, label="Сигнал с высококй частотой дискретизации")
    plt.plot(low_discretization_numbers, low_discretization_signal, "o", label="Сигнал с низкой частотой дискретизации")
    plt.plot(high_discretization_numbers, interpolated_signal, "--", label="Интерполянт")
    plt.legend()


def main():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.interpolate import lagrange, CubicSpline
    from statistics import stdev

    # Генерируем сигнал
    n = np.linspace(0, 2, N)
    signal_function = 'log(2 - cos(2 * pi * 3 * time))'
    generated_signal = signal_generate(n, signal_function)

    # Генерируем дискритизацию сигнала
    M = 40
    sd = np.linspace(0, 2, M)
    points_of_generated_signal = signal_generate(sd, signal_function)

    # Интерполяция методом лагранжа
    lagrange_interpolation = lagrange(sd, points_of_generated_signal)
    interpolation_signal_plot(generated_signal, n, points_of_generated_signal, sd, lagrange_interpolation(n), "полиномиальным")
    plt.savefig(f'Интерполяция методом лагранжа по {M} точек.png')

    # Кубическая интерполяция
    cubic_spline_interpolation = CubicSpline(sd, points_of_generated_signal)
    interpolation_signal_plot(generated_signal, n, points_of_generated_signal, sd, cubic_spline_interpolation(n), "кубическая")
    plt.savefig(f'Кубическая интерполяция по {M} точек.png')

    # Определяем величину относительной среднеквадратической ошибки интерполяции
    # Для полиномиальной интерполяции методом лагранжа
    delta_lagrange_interpolation = generated_signal - lagrange_interpolation(n)
    epsilon_lagrange = stdev(delta_lagrange_interpolation)/stdev(generated_signal)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(delta_lagrange_interpolation)
    ax.text(0, 0.5, "Среднеквадратическая ошибка интерполяции равна {}".format(epsilon_lagrange), transform=ax.transAxes, fontsize=15)

    # Для кубической интерполяции
    delta_spline_interpolation = generated_signal - cubic_spline_interpolation(n)
    epsilon_spline = stdev(delta_spline_interpolation)/stdev(generated_signal)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(delta_spline_interpolation)
    ax.text(0, 0.5, "Среднеквадратическая ошибка интерполяции равна {}".format(epsilon_spline), transform=ax.transAxes, fontsize=15)

    plt.show()


if __name__ == "__main__":
    main()
