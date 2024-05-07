# APLICANDO MÉTODOS E ALTERANDO VALORES

class Carro:
    def __init__(self, marca:str, modelo:str ,velocidade_maxima: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, vrum:int = 10):
        if self.velocidade_atual + vrum < self.velocidade_maxima:
            self.velocidade_atual += vrum
            return f"O carro {self.modelo} acelerou e está a {self.velocidade_atual}km por hora"
        else:
            return f"Tira o pé meu fi, quer bater o motor é? (vulgo: seu anjo da guarda)"
    
    def freiar(self):
        if self.velocidade_atual < 5:
            self.velocidade_atual = 0
            return f"O carro {self.modelo} parou"
        else:
            self.velocidade_atual -= 5
            return f"O carro {self.modelo} freiou e está a {self.velocidade_atual}km por hora"

carro1 = Carro(marca="Fiat", modelo="Uno", velocidade_maxima = 110)
carro2 = Carro(marca="Fiat", modelo="Toro", velocidade_maxima = 160)
carro3 = Carro(marca="Hyundai", modelo="HB20", velocidade_maxima = 160)


print(carro1.acelerar(vrum=15))
print(carro1.acelerar(vrum=20))
print(carro1.acelerar(vrum=50))
print(carro1.acelerar())
print(carro1.acelerar())
print(carro1.acelerar(vrum=50))
print(carro1.freiar())
print(carro1.freiar())
print(carro1.acelerar(vrum=10))
print(carro1.acelerar(vrum=20))