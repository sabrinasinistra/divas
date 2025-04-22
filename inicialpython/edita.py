#EXEMPLO DE CÓDIGO

#importa a biblioteca
import sqlite3

#Cria duas variáveis, conexão vai ser usada para acessar o arquivo, cursor vai ser usado para acessar coisas dentro do arquivo
conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()

#Cria um tipo de tabela. Aqui não é criado nenhum usuário, é só a definição de uma estrutura usada pra guardar dados
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, idade INTEGER)")

#Loop pra casos de criação de mais de um usuário por execução do programa
while True:
    #Recebe o nome
    nome_input = input("Nome: ")
    #recebe a idade
    idade_input = int(input("Idade :"))

    #Insere novas informações de usuário na nossa estrutura genérica e salva no arquivo
    cursor.execute("INSERT INTO usuarios(nome, idade) VALUES (?, ?)", (nome_input, idade_input))
    conexao.commit()

    #Recebe a confirmação de continuidade do loop, se a resposta for não, sai do loop
    continuidade = input("Deseja continuar? ")
    if continuidade == "Não":
        break;


#Um pouquinho mais complicado:
#cursor.execute retorna uma lista de todos os usuários cadastrados ordenados pelo id(de maior para menor)
#para cada linha na lista de usuários cadastrados, printa a linha
for linha in cursor.execute("SELECT id, nome FROM usuarios ORDER BY id"):
    print(linha)


conexao.close()





