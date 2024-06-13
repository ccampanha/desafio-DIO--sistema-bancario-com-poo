from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self, endereco):
        self.__endereco =  endereco
        self.__contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.__contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, agencia, cliente):
        self.__saldo = 0
        self.__numero = numero
        self.__agencia = agencia
        self.__cliente = cliente
        self.__historico = Historico()

    @classmethod #método de classe
    def nova_conta(cls, numero, agencia, cliente):
        return cls(numero, agencia, cliente)
 
    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def agencia(self):
        return self.__agencia
    
    def cliente(self):
        return self.__cliente
    
    def historico(self):
        return self.__historico
    
    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                self.__historico.registrar(f"Saque: R$ {valor:.2f}")
                return True
            else:
                print("Operação falhou! Saldo insuficiente.")
                return False
        else:
            print("Operação falhou! Não é possível sacar um valor negativo.")
            return False
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__historico.registrar(f"Depósito: R$ {valor:.2f}")
            return True
        else:
            print("Operação falhou! Não é possível depositar um valor negativo.")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite=500, limite_saques=3):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico().transacoes 
             if transacao.tipo == "saque"]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques
        if excedeu_limite:
            print("Operação falhou! O saque excede o limite.")
            return False
        
        if excedeu_saques:
            print("Operação falhou! O número de saques diários excede o limite permitido.")
            return False
        
        if valor > 0:
            if self.__saldo + self.__limite >= valor:
                self.__saldo -= valor
                self.__historico.registrar(f"Saque: R$ {valor:.2f}")
                return True
            else:
                print("Operação falhou! Saldo insuficiente.")
                return False
        else:
            print("Operação falhou! Não é possível sacar um valor negativo.")
            return False

    def _str_(self):
        return f"Agência: {self.agencia} - C/C: {self.numero} - Titular: {self.cliente.nome}"

class Historico:
    def __init__(self):
        self.__transacoes = []

    @property
    def transacoes(self):
        return self.__transacoes

    def registrar_transacao(self, transacao):
        self.__transacoes.append(
            {
                "tipo" : transacao._class_._name_,
                "valor" : transacao.valor,
                "data" : datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor (self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.registrar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.registrar_transacao(self)


def menu():
    menu = """\n
    =================  MENU  =================

    Digite o numero da operação desejada:
    1 - DEPOSITAR
    2 - SACAR
    3 - EMITIR EXTRATO
    4 - CRIAR USUARIO
    5 - CRIAR CONTA
    6 - LISTAR CONTA
    7 - SAIR
    
    ==========================================

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    pass


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    pass


def emitir_extrato():
   pass


def criar_cliente():
   pass


#def filtrar_usuario():
#    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
#    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta():
    pass
   # cpf = input("Informe o CPF do usuário: ")
   # usuario = filtrar_usuario(cpf)

   # if usuario:
   #     numero_conta = len(contas) + 1
   #     conta = Conta.nova_conta(numero_conta, AGENCIA, usuario)
   #     contas.append(conta)
   #     print("\n=== Conta criada com sucesso! ===")
   #     return conta

   # print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
   #   print("\n=== Conta criada com sucesso! ===")
   #   return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    #print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas():
   pass


def main():
    while True:
        opcao = menu()

        if opcao == "1":
            pass

        elif opcao == "2":
            pass

        elif opcao == "3":
           pass

        elif opcao == "4":
            pass

        elif opcao == "5":
           pass 

        elif opcao == "6":
            pass

        elif opcao == "7":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
main()