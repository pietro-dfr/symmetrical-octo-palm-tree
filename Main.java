/**
 * @grupo Pietro, Danilo, Erik
 */
//Uma classe serve pra criar novos tipos pra representar uma entidade 
// A classe Livro representa um modelo para entidade do livro
// Ela tem dois atributos: título e autor, que guardam informações básicas.
// O método mostrarInfo printa essas informações na tela.
// A classe Main cria um objeto da classe Livro e usa ele na prática.
// A classe é um molde ou planta pra criar objetos e organizar o codigo
class Livro {
    String titulo;
    String autor;

    public void mostrarInfo() {
        System.out.println("Título: " + titulo + ", Autor: " + autor);
    }
}
// O Encapsulamento serve para proteger os dados internos da classe.
// O atributo saldo está como "private", então só pode ser acessado de forma segura pela propia classe.
// Os métodos "deposita"r e "getSaldo" controlam como o valor é lido e alterado
// Isso impede alterações erradas ou inseguras no saldo da conta.
// Controla como os atributos sao alterados
class Conta {
    private double saldo;
    public void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
        }
    }

    public double getSaldo() {
        return saldo;
    }
}
// Herança permite que uma classe use atributos e métodos de outra classe.
// Aqui, Moto herda da classe Veiculo, ou seja, ela pode usar o método mover().
// A herança facilita o desenvolvimento sem reescrever código.
// É como copiar todo o codigo de uma classe e colocar em outra pelo "extends"(estende)
// Se uma classe herda de outra ela é uma especialização da superclasse
class Veiculo {
    public void mover() {
        System.out.println("andando...");
    }
}

class Moto extends Veiculo {
    public void empinar() {
        System.out.println("Grau");
    }
}
// Polimorfismo permite que objetos de classes diferentes usem o mesmo método de forma diferente.
// Tambem permite que eu trate varias especializações de uma classe da mesma forma
//Se eu criar um função que mexe com um animal ela funcionara com todos
//É o conceito de algo ter varias formas, como o metodo fazerSom()
//Que pode ter uma implementação diferente doque a da superclasse
class Animal {
    public void fazerSom() {
        System.out.println("algum som");
    }
}

class Gato extends Animal {
    @Override //Basicamente diz que esse metodo e diferente doque era antes(foi sobscrito)
    public void fazerSom() {
        System.out.println("miando");
    }
}
class Cachorro extends Animal {
    @Override
    public void fazerSom() {
        System.out.println("latindo");
    }
}
//Abstração é esconder oque é desnecessario e focar noque um objeto faz ao enves de como
// Quem usa essa classe só precisa chamar "enviarEmail".
// não precisamos saber como a conexão SMTP funciona, nem como o HTML do email é formatado.
// Pra tornar mais simples quem vai utilizar essa classe
// Isso deixa o sistema limpo, e mais simples de entender pra que as coisas servem
class EmailService {

    public void enviarEmail(String destinatario, String mensagem) {
        conectarSMTP();
        formatarMensagem(mensagem);
        enviar(destinatario, mensagem);
    }

    private void conectarSMTP() {
        System.out.println("Conectandooooo");
    }

    private void formatarMensagem(String mensagem) {
        System.out.println("Formatando a mensagem...");
    }

    private void enviar(String destinatario, String mensagem) {
        System.out.println("Enviando email para " + destinatario + ": " + mensagem);
    }
}


public class Main {
    public static void main(String[] args) {
        Livro livro1 = new Livro();
        livro1.titulo = "Coraline";
        livro1.autor = "Neil Gaiman";
        livro1.mostrarInfo();
        //
        Conta c = new Conta();
        c.depositar(500.0);
        System.out.println("Saldo disponível: R$ " + c.getSaldo());
        //
        Moto m = new Moto();
        m.mover();
        m.empinar();
        //
        Animal a1 = new Gato();
        Animal a2 = new Cachorro();
        a1.fazerSom();
        a2.fazerSom();
    }
}

