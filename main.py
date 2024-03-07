"""Generar un plot para distintos valores de R, C y V (ingresados por el usuario)"""

# Se importan los modulos necesarios: Numpy, Matplotlib, Scipy
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate


def graficar_carga(funcion, R, C, V, labels):
    # Se hacen los calculos previos, se definen las funciones.
    if "Carga (C)" in labels[2]:
        y_max = C * V
    elif "Voltaje (V)" in labels[2]:
        y_max = V
    elif "Intensidad de corriente (A)" in labels[2]:
        y_max = V / R
    t_max = t_max = -(R * C * np.log(0.01))
    t = np.linspace(0, t_max, 1000)
    sol = scipy.integrate.odeint(funcion, 0, t, args=(R, C, V,))
    """t_max_conseguido = False
    t_max = 1
    while not t_max_conseguido:
        t = np.linspace(0, t_max, 1000)
        sol = scipy.integrate.odeint(funcion, 0, t, args=(R, C, V,))
        if sol[-1] >= 0.999 * y_max:
            t_max_conseguido = True
        else:
            t_max += 1"""
    q_max = sol[-1]
    # Se crea la figura base.
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(t, sol)

    # Se añaden las etiquetas y limites.
    ax.set(xlabel=labels[1], ylabel=labels[2],
           title=labels[0])
    ax.set_xlim(0, t_max)
    ax.set_ylim(0, 1.05 * q_max)
    ax.grid()
    plt.text(1 * t_max, 1.01 * 1.05 * (q_max), "Programado por Enrique Corvalan", ha="right", fontsize=10, color=".5")

    # Se retorna la figura.
    return fig, ax


def graficar_descarga(funcion, R, C, V, labels):
    # Se hacen los calculos previos, se definen las funciones.
    if "Carga (C)" in labels[2]:
        y0 = C * V
    elif "Voltaje (V)" in labels[2]:
        y0 = V
    elif "Intensidad de corriente (A)" in labels[2]:
        y0 = V / R
    t_max = -R * C * np.log((0.001) / (C * V))
    t = np.linspace(0, t_max, 1000)
    sol = scipy.integrate.odeint(funcion, y0, t, args=(R, C, V,))
    """t_max_conseguido = False
    t_max = 1
    while not t_max_conseguido:
        print(t_max)
        t = np.linspace(0, t_max, 1000)
        sol = scipy.integrate.odeint(funcion, y0, t, args=(R, C, V,))
        if t_max >= 10000:
            # Si los valores introducidos son muy altos, se demora demasiado.
            # En ese caso se calcula de antemano el t_max a mostrar.
            t_max = -R * C * np.log((0.001) / (C * V))
            t_max_conseguido = True
        elif sol[-1] <= 0.001:
            t_max_conseguido = True
        else:
            t_max += 1"""
    y_max = y0
    # Se crea la figura base.
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(t, sol)

    # Se añaden las etiquetas y limites.
    ax.set(xlabel=labels[1], ylabel=labels[2],
           title=labels[0])
    ax.set_xlim(0, t_max)
    ax.set_ylim(0, 1.05 * y_max)
    ax.grid()
    plt.text(1 * t_max, 1.01 * 1.05 * (y_max), "Programado por Enrique Corvalan", ha="right", fontsize=10, color=".5")

    # Se retorna la figura.
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
        print("¡Introduzca un numero!")
        return preguntar_float(texto)
    else:
        return respuesta_float


def preguntar_tipo():
    respuesta = input("¿Quiere un grafico de carga [1] o descarga [2]?: ")
    if respuesta not in ["1", "2"]:
        print("¡Ingrese una respuesta válida!")
        return preguntar_tipo()
    elif respuesta == "1":
        return "CARGA"
    elif respuesta == "2":
        return "DESCARGA"


if __name__ == "__main__":
    """# DEV INPUTS
    tipo = "CARGA
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
    tipo = preguntar_tipo()
    if tipo == "CARGA":
        quiere_q = preguntar_sn("¿Quiere un grafico de Carga vs Tiempo?")
        quiere_v = False
        quiere_i = False
        if not quiere_q:
            quiere_v = preguntar_sn("¿Quiere un grafico de Voltaje vs Tiempo?")
        if not quiere_q and not quiere_v:
            quiere_i = preguntar_sn("¿Quiere un grafico de Intensidad de corriente vs Tiempo?")
        if any((quiere_q, quiere_v, quiere_i)):
            R = preguntar_float("Indique el valor de la resistencia (Ohm): ")
            C = preguntar_float("Indique el valor de la capacitancia (Farad): ")
            V = preguntar_float("Indique el voltaje suministrado por la fuente (Volt): ")
            if quiere_q:
                figq, axq = graficar_carga(lambda q, t, R, C, V: (C * V - q) / (R * C), R, C, V, ("Gráfico carga condensador: Carga vs Tiempo", "Tiempo [s]", "Carga (C)"))
            if quiere_v:
                figv, axv = graficar_carga(lambda v, t, R, C, V: (V - v) / (R * C), R, C, V, ("Gráfico carga condensador: Voltaje vs Tiempo", "Tiempo [s]", "Voltaje (V)"))
            if quiere_i:
                figi, axi = graficar_carga(lambda i, t, R, C, V: (V - i * R) / (R * R * C), R, C, V, ("Gráfico carga condensador: Intensidad de corriente vs Tiempo", "Tiempo [s]", "Intensidad de corriente (A)"))
            # Se muestran las figuras.
            plt.show()
    elif tipo == "DESCARGA":
        quiere_q = preguntar_sn("¿Quiere un grafico de Carga vs Tiempo?")
        quiere_v = False
        quiere_i = False
        if not quiere_q:
            quiere_v = preguntar_sn("¿Quiere un grafico de Voltaje vs Tiempo?")
        if not quiere_q and not quiere_v:
            quiere_i = preguntar_sn("¿Quiere un grafico de Intensidad de corriente vs Tiempo?")
        if any((quiere_q, quiere_v, quiere_i)):
            R = preguntar_float("Indique el valor de la resistencia (Ohm): ")
            C = preguntar_float("Indique el valor de la capacitancia (Farad): ")
            V = preguntar_float("Indique el voltaje suministrado por la fuente (Volt): ")
            if quiere_q:
                figq, axq = graficar_descarga(lambda q, t, R, C, V: (-q) / (R * C), R, C, V, ("Gráfico descarga condensador: Carga vs Tiempo", "Tiempo [s]", "Carga (C)"))
            if quiere_v:
                figv, axv = graficar_descarga(lambda v, t, R, C, V: (-v) / (R * C), R, C, V, ("Gráfico descarga condensador: Voltaje vs Tiempo", "Tiempo [s]", "Voltaje (V)"))
            if quiere_i:
                figi, axi = graficar_descarga(lambda i, t, R, C, V: (-i) / (R * C), R, C, V, ("Gráfico descarga condensador: Intensidad de corriente vs Tiempo", "Tiempo [s]", "Intensidad de corriente (A)"))
            # Se muestran las figuras.
            plt.show()
