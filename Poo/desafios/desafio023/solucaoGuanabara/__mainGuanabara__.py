from rich import print, inspect
from poligonoGuanabara import *

def main():
    p1 = Quadrado(12)
    c = Circulo(12)
    inspect(p1,methods=True)
    inspect(c,methods=True)
    print(f" Um quadrado de lado {p1.lado}m tem Perimetro de {p1.perimetro():.1f} m")
    print(f" Um quadrado de lado {p1.lado}m tem Area = {p1.area():.1f} m²")
    print(f"Um círculo de raio {c.raio}m tem Perimetro = {c.perimetro():.1f} m")
    print(f"Um círculo de raio {c.raio}m tem Area = {c.area():.1f} m²")

if __name__ == "__main__":
    main()