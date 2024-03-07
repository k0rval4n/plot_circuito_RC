# Tarea 7: Plot de un circuito RC ⚡

Aplicación solicitada en el curso IEE1533 "Fundamentos de la Teoría Electromagnética" 2023-2.

## Enunciado:
Escribir un programa que, resolviendo numéricamente las ecuaciones diferenciales de carga y descarga de una capacitancias en un circuito RC, genere un plot parecido al de la clase para distintos valores de R [resistencia] y de C [capacitancia] (ingresados por el usuario). Pueden representar q(t), o v(t), o i(t), o incluso las tres cantidades.

Lenguaje utilizado: ```Python```

## Librerías utilizadas: 📚
- ```numpy```
- ```matplotlib```
- ```scipy```

## Funcionamiento programa: 🤓
    Aprendido manejo de excepciones 😎
Se le solicita al usuario introducir los datos necesarios mediante consola en el siguiente orden:
1. Tipo de gráfico I: carga [1] o descarga [2]
2. Tipo de gráfico II: Sí [S] o No [N]
    - Carga v/s Tiempo
    - Voltaje v/s Tiempo
    - Intensidad de corriente v/s Tiempo
3. Valor de la resistencia
4. Valor de la capacitancia
5. Valor del voltaje suministrado por la fuente


\* El Programa espera recibir ```float``` en los inputs [```3.```](#L23), [```4.```](#L24) y [```5.```](#L25).

Finalmente, se abrirá una nueva ventana mostrando el gráfico solicitado.