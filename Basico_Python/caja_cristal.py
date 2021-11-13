import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):

    def test_es_mayor_de_edad(self):
        edad =20 
        #envia el valor para probar la función y almacenar en resultado
        resultado=es_mayor_de_edad(edad)
        #es correcto si es True
        self.assertEqual(resultado,True)


    def test_es_menor_de_edad(self):
        edad =15 
        #envia el valor para probar la función y almacenar en resultado
        resultado=es_mayor_de_edad(edad)
        #es correcto si es False
        self.assertEqual(resultado,False)


if __name__ == "__main__":
    unittest.main(verbosity=2)