class Cliente:
    def __init__(self,nome, anoNascimento, sexo, saldo, endereco, ativo):
        self.nome = nome
        self.anoNascimento = anoNascimento
        self.sexo = sexo
        self.saldo = saldo
        self.endereco = endereco
        self.ativo = ativo
       
    def imprimir(self):
        print("----------------------")
        print("nome:",self.nome)
        print("anoNascimento:", self.anoNascimento)
        print("sexo:",self.sexo)
        print("saldo:", self.saldo)
        print("endereco:", self.endereco)
        print("ativo:", self.ativo)
   
    def verificaClienteAtivo(self):
        print("----------------------")
        if self.ativo == True:
            print("O cliente", self.nome, "está ativo")
        else:
            print("O cliente", self.nome, "está inativo")

    def calcularIdade(self):
          print("----------------------")
          anoAtual = 2024
          idade = (anoAtual-self.anoNascimento)
          print("A Idade do Cliente é", idade)

    def verificar_saldo(self):
        print("----------------------")
        if self.saldo >= 0:
            print("O Saldo", self.saldo,"é positivo")
        else:
             print("O saldo", self.saldo,"é negativo")




cliente1 = Cliente("Stefhany", 2006, "Feminino", 10000, "Rua Teste", True)
cliente2 = Cliente("Mahya", 2020, "Feminino", -5000, "Rua Teste", True)
cliente3 = Cliente("Odair", 1981, "Masculino", 15000, "Rua Teste", False)

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()

cliente1.verificaClienteAtivo()
cliente2.verificaClienteAtivo()
cliente3.verificaClienteAtivo()

cliente1.calcularIdade()
cliente2.calcularIdade()
cliente3.calcularIdade()

cliente1.verificar_saldo()
cliente2.verificar_saldo()
cliente3.verificar_saldo()







       
 
