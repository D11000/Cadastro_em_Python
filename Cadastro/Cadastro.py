def cadastro():
    cadastrar =str(input("Digite o nome do aluno que voce deseja cadstrar :"))

    with open("arqcad.txt",'a')as arquivo:
        cadastrar = cadastrar + '\n'
        arquivo.write(cadastrar)
        cadastrar = cadastrar + '\n'

cadastro()
