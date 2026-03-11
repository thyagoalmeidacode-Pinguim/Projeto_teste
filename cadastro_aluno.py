# Sistema simples de cadastro de alunos

# Solicitação de dados
nome = input("Digite o nome do aluno: ")
idade = input("Digite a idade do aluno: ")
curso = input("Digite o curso do aluno: ")
email = input("Digite o email do aluno: ")

# Abertura do arquivo para salvar os dados
arquivo = open("cadastro_alunos.txt", "a")

# Escrita das informações no arquivo
arquivo.write("Nome: " + nome + "\n")
arquivo.write("Idade: " + idade + "\n")
arquivo.write("Curso: " + curso + "\n")
arquivo.write("Email: " + email + "\n")
arquivo.write("-----------------------------\n")

# Fechamento do arquivo
arquivo.close()

print("Cadastro realizado com sucesso!")