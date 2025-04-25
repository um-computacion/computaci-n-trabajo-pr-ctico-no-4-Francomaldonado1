def factorial_iterativo(n):  # definimos la funcion que calcula el factorial de un numero n de forma iterativa
    if n < 0:  
        raise ValueError("El factorial no está definido para números negativos.")  # n debe ser mayor o igual a 0
    resultado = 1  
    for i in range(2, n + 1):  
        """  Este proceso utiliza un bucle para multiplicar todos los enteros desde 2 hasta n (inclusive).  
        Se inicia desde 2, ya que el factorial de 0 y 1 es 1.   
        En cada iteración, el resultado se actualiza multiplicando por el número actual i,  
        lo que permite construir el factorial de n de manera acumulativa. """
        resultado *= i  
    return resultado  

def factorial_recursivo(n):  # definimos la funcion que calcula el factorial de un numero n de forma recursiva
    if n < 0:  
        raise ValueError("El factorial no está definido para números negativos.")  # n debe ser mayor o igual a 0
    if n == 0 or n == 1:  
        return 1  
    return n * factorial_recursivo(n - 1)  
        