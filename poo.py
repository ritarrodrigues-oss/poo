class Estudante:
    def __init__(self, nome, nota1, nota2):
       self.nome = nome
       self.nota1 = nota1
       self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        media = (self.nota1 + self.nota2) / 2
        if media >= 6:
            return "Aprovado"
        elif media >= 4:
            return "Recuperação"
        return "Reprovado"

    def descrever(self):
        return (f"{self.nome:<16} {self.nota1:<7.1f} {self.nota2:<7.1f} {self.media():<8.1f} {self.situacao():<14}")

    def cadastrar():
        nome = input("Nome do estudante:")
        nota1 = float(input("Nota 1:"))
        nota2 = float(input("Nota 2:"))

        Estudante.append(Estudante(nome, nota1, nota2))
        print("Estudante cadastrado")

    def listar(estudantes):
        if len(estudantes) == 0:
            print("Nenhum estudante cadastrado")
            return

        print(f"\n{'Nome do estudante':<16} {'N1':<7} {'N2':<7} {'MÉDIA':<8} {'SITUAÇÃO':<14}")

        for estudante in estudantes:
            print(estudante.descrever())

    def media_da_turma():    
        if len(estudante) == 0:
            print("Nenhum estudante cadastrado")
            return
        
        soma = 0

        for estudante in estudantes:
            soma = soma = estudante.media()
        print(f"Média da turma: {soma / len(estudante):.2f}")

        def menu():
            while True:
                print("\n1 - Cadastrar estudante")
                print("2 - Listar estudantes")
                print("3 - Média da turma")
                print("0 - Sair")          

                opcao = input("Opção: ")

                if opcao == "1":
                    cadastrar()
                elif opcao == "2":
                    listar(estudantes)
                elif opcao == "3":
                    media_da_turma()
                elif opcao == "0":
                    break
                else:  print("Opção inválida")

menu()
