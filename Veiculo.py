class Veiculo:
    def _init_(self, marca, modelo, ano):
       self.marca = marca
       self.modelo = modelo
       self.ano = ano

    def ligar(self):
        print("Veículo ligado")

    def desligar(self):
        print("Veículo desligado")

class Carro(Veiculo):
    def _init_(self, marca, modelo, ano, numeroDePortas):
        super()._init_(marca, modelo, ano)
        self.numeroDePortas = numeroDePortas

    def NumeroDePortas(self):
        print("O Carro possui:", self.numeroDePortas)

class Moto(Veiculo):
    def _init_(self, marca, modelo, ano, cilindrad):
        super()._init_(marca, modelo, ano)
        self.cilindradas = cilindradas
    
    def Cilindradas(self):
        print("A Moto possui:", self.cilindradas)
      
Veiculo = Veiculo("Toyota, Corolla, 2024, 4")
Carro = Carro ("Chevrolet, Tracker, 2022, 4")
Moto = Moto ("Honda, Twister, 2024, 293,5")

Veiculo.imprimir()
Carro.imprimir()
Moto.imprimir()


