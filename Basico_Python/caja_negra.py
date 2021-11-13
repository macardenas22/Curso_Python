import unittest #libreria que permite generar pruebas unitarias

#se crean las funciones respectivas para el proceso de pruebas 
def suma(num_1,num_2):
    return num_1+num_2


#esta será denominada como la ejecución principal en vez de run()
#creamos una clase denominada caja negra cuya función esta asociada a un test de prueba de la libreria 
class CajaNegraTest(unittest.TestCase): 
    
    #creaos el primer caso de prueba por función y siempre se nombrará la función iniciando por test y un parametro self
    def test_suma_dos_positivos(self):
        num_1 = 10 
        num_2 = 5

        resultado = suma(num_1, num_2)
        #permite verificar y asegurar que el valor final de resultado sea 15 en el test
        self.assertEqual(resultado,15)


    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7
        resultado = suma(num_1, num_2)

        self.assertEqual(resultado,-17)



#esta rama es aparte, donde if name (nombre del modulo es igual a main se ejecuta la opción unittest) 
if __name__ == "__main__": 
    #ejecuta la función main de unittest y el parametro verbosity=2 permite ver algo más de detalle de la prueba
    unittest.main(verbosity=2) 