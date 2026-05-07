#Crie classes capazes de calcular fretes de veículos diferentes.
from rich import print

from drone import Drone
from moto import Moto
from caminhao import Caminhao
from rich.table import Table
def main():
    dist = 100
    drone = Drone(dist)
    caminhao = Caminhao(dist)
    moto = Moto(dist)


    table = Table(title="Tabela de Preços")
    table.add_column("Distância")
    table.add_column("Tipo")
    table.add_column("Frete")
    table.add_row(f"{dist}km",f"{type(moto).__name__}",f"{moto.calc_frete()}")
    table.add_row(f"{dist}km",f"{type(caminhao).__name__}",f"{caminhao.calc_frete()}")
    table.add_row(f"{dist}km",f"{type(drone).__name__}",f"{drone.calc_frete()}")
    print(table)
if __name__ == "__main__":
        main()