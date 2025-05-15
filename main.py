#Grupo: Pietro, Danilo, Erik
#Esse arquivo Erik e Danilo fizeram juntos
#1- Classe e objeto: Uma classe é como um molde ou modelo.Ela
# define como os objetos serão, ou seja, quais atributos (dados)
# e métodos (ações) eles terão; Um objeto é uma instância
# (exemplo real) da classe. Ele usa o modelo da classe para existir
# com dados próprios.

#Classe base, onde se tem alguns objetos
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def exibir_info(self):
        print(f"{self.marca} {self.modelo}")
#Usando esses objetos da classe
meu_carro = Carro("Toyota", "Corolla")
meu_carro.exibir_info()

#2- Atributo e método: Um atributo é uma característica de um objeto.
# Ele armazena dados (informações) sobre o objeto.
# Exemplo: nome, idade, cor, tamanho; Um método é uma função dentro
# de uma classe.Ele representa um comportamento do objeto (algo que ele faz).
# Exemplo: andar, falar, apresentar.

class Pessoa:
    #Atributos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    #Método 
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
#Usando os métodos
p1 = Pessoa("Ana", 25)
p1.apresentar()

#3- Encapsulamento: O encapsulamento é um conceito da programação
# orientada a objetos que significa esconder os detalhes internos
# de uma classe e proteger os dados, permitindo o acesso apenas por
# métodos específicos.

class ContaBancaria:
    #Dado escondido/encapsulado
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    #Dado escondido/encapsulado
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    #Metódo para usar os dados encapsulados 
    def exibir_saldo(self):
        print(f"Saldo de {self.titular}: R${self.__saldo:.2f}")
#Usando os dados encapsulados pelos métodos 
conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.exibir_saldo()

#4- Herança: Herança é um conceito da programação orientada a objetos
# que permite uma classe herdar características e comportamentos de outra.
# Ou seja, uma classe "filha" (ou subclasse) pode reutilizar o que já existe
# em uma classe "pai" (ou superclasse).

# Classe base
class Pessoa:
    def falar_ola(self):
        print("Olá! Eu sou um estudante.")
# Classe derivada
class Estudante(Pessoa):
    def estudar(self):
        print("Estou estudando agora!")
# Criando um estudante
justos = Estudante()
# Usando os métodos das classes
justos.falar_ola()   # Herança da classe Pessoa
justos.estudar()     # Método ou ação da classe Estudante

#5- Polomorfismo: O polimorfismo na programação orientada a objetos,
# permite que diferentes classes tenham métodos com o mesmo nome,
# mas com comportamentos diferentes.

class Cachorro:
    def falar(self):
        print("O cachorro diz: Au au!")
class Gato:
    def falar(self):
        print("O gato diz: Miau!")
# Função que usa polimorfismo das classes
def fazer_animal_falar(animal):
    animal.falar()
# Criando os objetos das funções 
c1 = Cachorro()
g1 = Gato()
# Usando a função com diferentes tipos
fazer_animal_falar(c1)  # Saída sera: O cachorro diz: Au au!
fazer_animal_falar(g1)  # Saída sera: O gato diz: Miau!

#6- Abstração: Uma classe de abstração (ou classe abstrata) é uma classe que
# serve como modelo para outras classes. Ela não pode ser usada diretamente
# para criar objetos. Em vez disso, outras classes herdam dela e implementam
# os métodos que ela define como obrigatórios.

from abc import ABC, abstractmethod
# Classe abstrata, uma classe geral
class Forma(ABC):
    @abstractmethod
    def desenhar(self):
        pass
# Classe concreta, filha da abstrata
class Circulo(Forma):
    def desenhar(self):
        print("Desenhando um círculo.")
# Classe concreta, filha da abstrata
class Quadrado(Forma):
    def desenhar(self):
        print("Desenhando um quadrado.")
# Usando as classes
forma1 = Circulo()
forma2 = Quadrado()
forma1.desenhar()  # Saída sera: Desenhando um círculo.
forma2.desenhar()  # Saída sera: Desenhando um quadrado.