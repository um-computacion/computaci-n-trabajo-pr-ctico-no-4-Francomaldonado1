import unittest  

def factorial_iterativo(n):  
    if n < 0:  
        raise ValueError("El factorial no está definido para números negativos.")  
    resultado = 1  
    for i in range(2, n + 1):  
        resultado *= i  
    return resultado  

def factorial_recursivo(n):  
    if n < 0:  
        raise ValueError("El factorial no está definido para números negativos.")  
    if n == 0 or n == 1:  
        return 1  
    return n * factorial_recursivo(n - 1)  

class TestFactorial(unittest.TestCase):  
    
    def test_factorial_iterativo(self):  
        self.assertEqual(factorial_iterativo(0), 1)     
        self.assertEqual(factorial_iterativo(1), 1) 
        self.assertEqual(factorial_iterativo(5), 120)   
        self.assertEqual(factorial_iterativo(10), 3628800) 
        self.assertEqual(factorial_iterativo(20), 2432902008176640000)
        self.assertEqual(factorial_iterativo(25), 15511210043330985984000000)

    def test_factorial_recursivo(self):  
        self.assertEqual(factorial_recursivo(0), 1)     
        self.assertEqual(factorial_recursivo(1), 1)      
        self.assertEqual(factorial_recursivo(5), 120)   
        self.assertEqual(factorial_recursivo(10), 3628800) 
        self.assertEqual(factorial_recursivo(20), 2432902008176640000)
        self.assertEqual(factorial_recursivo(25), 15511210043330985984000000)

    def test_factorial_negativo(self):  
        with self.assertRaises(ValueError):  
            factorial_iterativo(-1)  
        with self.assertRaises(ValueError):  
            factorial_recursivo(-1)   
        with self.assertRaises(ValueError):
            factorial_iterativo(-10)
        with self.assertRaises(ValueError):
            factorial_recursivo(-10)
        with self.assertRaises(ValueError):
            factorial_iterativo(-20)
        with self.assertRaises(ValueError):
            factorial_recursivo(-20)

if __name__ == '__main__':  
    unittest.main()  
    

