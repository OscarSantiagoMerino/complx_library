import Tareacomplx as tc
import unittest

class TestStringMethods(unittest.TestCase):

    def test_complxsuma(self):
        suma1 = tc.complxsuma((3,5),(4,6))
        num1 = 7
        num2 = 11
        num3 = -5
        suma2 = tc.complxsuma((3,1),(-8,-6))
        self.assertAlmostEqual(suma1,f"el resultado de la suma de los numeros complejos es :{num1},{num2}i")
        self.assertAlmostEqual(suma2,f"el resultado de la suma de los numeros complejos es :{num3},{num3}i")
    def test_complxproducto(self):
        producto1 = tc.complxproducto((2,4),(4,-1))
        num1 = 12
        num2 = 14
        num3 = -6
        num4 = 1
        producto2 = tc.complxproducto((0,1),(1,6))
        self.assertAlmostEqual(producto1, f"el resultado del producto de los numeros complejos es :{num1},{num2}i")
        self.assertAlmostEqual(producto2, f"el resultado del producto de los numeros complejos es :{num3},{num4}i")
    def test_complxresta(self):
        resta1 = tc.complxresta((2,2),(0,-1))
        num1 = 2
        num2 = 3
        num3 = 1
        num4 = -3
        resta2 = tc.complxresta((0,5),(-1,8))
        self.assertAlmostEqual(resta1, f"el resultado de la resta de los numeros complejos es :{num1},{num2}i")
        self.assertAlmostEqual(resta2, f"el resultado de la resta de los numeros complejos es :{num3},{num4}i")
    def test_complxdivision(self):
        division1 = tc.complxdivision((3,2),(8,1))
        num1 = 0.4
        num2 = 0.2
        num3 = -0.8
        num4 = -0.4
        division2 = tc.complxdivision((0,2),(-1,-2))
        self.assertAlmostEqual(division1, f"el resultado de la division de los numeros complejos es :{num1},{num2}i")
        self.assertAlmostEqual(division2, f"el resultado de la division de los numeros complejos es :{num3},{num4}i")
    def test_complxmodulo(self):
        modulo1 = tc.complxmodulo((4,-3))
        num1 = 5.0
        num2 = 16.0
        modulo2 = tc.complxmodulo((0,-16))
        self.assertAlmostEqual(modulo1, f"el resultado del modulo de tu numero complejo es {num1}")
        self.assertAlmostEqual(modulo2, f"el resultado del modulo de tu numero complejo es {num2}")
    def test_complxconjugado(self):
        conjugado1 = tc.complxconjugado((0,-1))
        num1 = 0
        num2 = 1
        num3 = 3
        num4 = -4
        conjugado2 = tc.complxconjugado((3,4))
        self.assertAlmostEqual(conjugado1, f"el resultado del conjugado de tu numero complejo es {num1},{num2}i")
        self.assertAlmostEqual(conjugado2, f"el resultado del conjugado de tu numero complejo es {num3},{num4}i")
    def test_complxpolarcarter(self):
        polarcarter1 = tc.complxpolarcarter((3,45))
        num1 = 1.57597
        num2 = 2.55271
        num3 = 0.0
        polarcarter2 = tc.complxpolarcarter((0,-24))
        self.assertAlmostEqual(polarcarter1, f"al pasar de polar a carteciano tu numero complejo el resultado es {num1},{num2}i")
        self.assertAlmostEqual(polarcarter2, f"al pasar de polar a carteciano tu numero complejo el resultado es {num3},{num3}i")
    def test_complxfase(self):
        fase1 = tc.complxfase((10,31))
        num1 = 1.25875
        num2 = -1.46592
        fase2 = tc.complxfase((2,-19))
        self.assertAlmostEqual(fase1,f"el valor de la fase de ese numero complejo es:{num1}")
        self.assertAlmostEqual(fase2,f"el valor de la fase de ese numero complejo es:{num2}")
if __name__ == '__main__':
    unittest.main()