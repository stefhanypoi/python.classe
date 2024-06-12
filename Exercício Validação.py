class Cadastro:
    Nome = None
    def __init__(self) -> None:
        pass

    def InserirNome (self, nome):
        nomePreenchido = self.ValidaNome (nome)
        if nomePreenchido == True:
            self.nome = nome 
            print("nome não pode estar vazio")
    
    def ValidaNome(self, nome):
        if len(nome) == 0 :
            print("Cadastrado com suceso")
            return False
        else:
            return True
        
    def InserirIdade(self, idade):
        idadeCorreta =  self. Validade(idade)
        if idadeCorreta == True:
            self.idade = idade
            print("idade precisa ser maio que 18")

    def ValidadeIdade(self, idade):
        if idade > 18:
            print("Valor cadastrado com suceso")
            return False
        else:
            return True
        
    def InserirSaldo(self, saldo):
        saldoCorreto = self.ValidadeSaldo (saldo)
        if saldoCorreto == True:
             self. saldo = saldo
             print("Valor cadastro não pode ser negativo")

    def ValidaSaldo(self,saldo):
        if saldo <0:
            print("Saldo positivo")
            return False
        else:
            return True
        

    cad = Cadastro()
    cad.InserirIdade(17)
    cad.InserirSaldo(500)
    cad.InserirNome(Stefhany)
    
    
        

  
