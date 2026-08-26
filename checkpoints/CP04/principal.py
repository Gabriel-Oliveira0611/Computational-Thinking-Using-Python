from cadastroPet import petCreate, petDelete, petList, petRead, petUpdate
from petsDB import db_pets


def exibir_menu() -> None:
    """Apresenta as opções disponíveis no sistema."""
    print("\nCADASTRO DE PETS")
    print(50 * "-")
    print("1 - Listar todos os pets")
    print("2 - Buscar pet")
    print("3 - Cadastrar pet")
    print("4 - Descadastrar pet")
    print("5 - Atualizar pet")
    print("6 - Sair")
    print(50 * "-")


def principal() -> None:
    """Executa o menu principal do CRUD de pets."""
    cadastro_pets = db_pets

    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite somente o número de uma das opções do menu.")
            continue

        match opcao:
            case 1:
                petList(cadastro_pets)

            case 2:
                identificador = input(
                    "Digite o ID completo, o registro ou o nome do pet: "
                )
                petRead(cadastro_pets, identificador)

            case 3:
                try:
                    nome = input("Nome do pet: ").strip()
                    tipo = input(
                        "Tipo (Cachorro, Gato, Mamífero, Ave, Réptil ou Outro): "
                    ).strip()
                    ano = int(input("Ano de nascimento: "))
                    cadastro_pets = petCreate(cadastro_pets, tipo, ano, nome)
                except (TypeError, ValueError) as erro:
                    print(f"Não foi possível cadastrar o pet: {erro}")

            case 4:
                id_pet = input("Digite o ID completo ou o registro do pet: ")
                cadastro_pets = petDelete(cadastro_pets, id_pet)

            case 5:
                id_pet = input("Digite o ID completo ou o registro do pet: ")
                cadastro_pets = petUpdate(cadastro_pets, id_pet)

            case 6:
                print("Programa encerrado.")
                break

            case _:
                print("Opção inválida. Escolha um número de 1 a 6.")


if __name__ == "__main__":
    principal()
