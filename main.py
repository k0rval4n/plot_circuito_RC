"""Generar un plot para distintos valores de R, C y V (ingresados por el usuario)"""

# Se importan los modulos necesarios: Numpy, Matplotlib
import numpy as np
import matplotlib.pyplot as plt


def graficar_q(R, C, V):
    # Se hacen los calculos previos, se definen las funciones.
    t_max = -(R * C * np.log(0.01))
    q_max = C * V
    t_salto = t_max/1000
    t = np.arange(0, t_max, t_salto)
    q = C * V * (1 - np.exp(-(t / (R * C))))

    # Se crea la figura base.
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(t, q)

    # Se añaden las etiquetas y limites.
    ax.set(xlabel='Tiempo (s)', ylabel='Carga (C)',
           title='Grafico Carga vs Tiempo')
    ax.set_xlim(0, t_max)
    ax.set_ylim(0, q_max)
    ax.grid()
    plt.text(1 * t_max, 1.01 * (q_max), "Programado por Enrique Corvalan", ha="right", fontsize=10, color=".5")

    # Se retorna la figura.
    return fig, ax


def graficar_v(R, C, V):
    # Se hacen los calculos previos, se definen las funciones.
    t_max = -(R * C * np.log(0.01))
    v_max = V
    t_salto = t_max/1000
    t = np.arange(0, t_max, t_salto)
    v = V * (1 - np.exp(-(t / (R * C))))

    # Se crea la figura base.
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(t, v)

    # Se añaden las etiquetas y limites.
    ax.set(xlabel='Tiempo (s)', ylabel='Voltaje (V)',
           title='Grafico Voltaje vs Tiempo')
    ax.set_xlim(0, t_max)
    ax.set_ylim(0, v_max)
    ax.grid()
    plt.text(1 * t_max, 1.01 * (v_max), "Programado por Enrique Corvalan", ha="right", fontsize=10, color=".5")

    # Se retorna la figura.
    return fig, ax


def graficar_i(R, C, V):
    # Se hacen los calculos previos, se definen las funciones.
    t_max = -(R * C * np.log(0.01))
    i_max = V / R
    t_salto = t_max/1000
    t = np.arange(0, t_max, t_salto)
    i = (V / R) * (1 - np.exp(-(t / (R * C))))

    # Se crea la figura base.
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(t, i)

    # Se añaden las etiquetas y limites.
    ax.set(xlabel='Tiempo (s)', ylabel='Intensidad de corriente (A)',
           title='Grafico Intensidad de corriente vs Tiempo')
    ax.set_xlim(0, t_max)
    ax.set_ylim(0, i_max)
    ax.grid()
    plt.text(1 * t_max, 1.01 * (i_max), "Programado por Enrique Corvalan", ha="right", fontsize=10, color=".5")

    # Se muestra la figura.
    return fig, ax


def preguntar_sn(texto):
    respuesta = input(f"{texto} [S / N]: ")
    if respuesta.upper() not in ["S", "N"]:
        print("¡Ingrese una respuesta valida!")
        return preguntar_sn(texto)
    elif respuesta.upper() == "S":
        return True
    else:
        return False


def preguntar_float(texto):
    respuesta = input(f"{texto}: ")
    try:
        respuesta_float = float(respuesta)
    except ValueError:
        print("¡Introduzca un numero")
        return preguntar_float(texto)
    else:
        return respuesta_float


if __name__ == "__main__":
    """# DEV INPUTS
    quiere_q = True
    quiere_v = True
    quiere_i = True
    R = 10.0
    C = 0.0001
    V = 220.0
    """
    # Inicia programa.
    # Se consulta el tipo de grafico a mostrar.
    # Si el interprete no deja introducir inputs, comentar esta seccion (""") e introducir manualmente los DEV INPUTS  en el codigo.
    quiere_q = preguntar_sn("¿Quiere un grafico de Carga vs Tiempo?")
    quiere_v = preguntar_sn("¿Quiere un grafico de Voltaje vs Tiempo?")
    quiere_i = preguntar_sn("¿Quiere un grafico de Intensidad de corriente vs Tiempo?")
    if any((quiere_q, quiere_v, quiere_i)):
        R = preguntar_float("Indique el valor de la resistencia (Ohm): ")
        C = preguntar_float("Indique el valor de la capacitancia (Farad): ")
        V = preguntar_float("Indique el voltaje suministrado por la fuente (Volt): ")
        if quiere_q:
            figq, axq = graficar_q(R, C, V)
        if quiere_v:
            figv, axv = graficar_v(R, C, V)
        if quiere_i:
            figi, axi = graficar_i(R, C, V)
        # Se muestran las figuras.
        plt.show()
