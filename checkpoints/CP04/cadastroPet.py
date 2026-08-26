from checaCadastroPet import checaCadastroPET


def _normalizar_tipo(tipo_pet: str) -> tuple | None:
    """Converte o tipo informado para código e descrição padronizados."""
    if not isinstance(tipo_pet, str):
        return None

    tipo = tipo_pet.strip().lower()

    match tipo:
        case "cc" | "cachorro" | "cão" | "cao" | "cães" | "caes":
            return "CC", "Cachorro"
        case "gt" | "gato" | "gata" | "gatos" | "gatas":
            return "GT", "Gato"
        case "mm" | "mamífero" | "mamifero" | "mamíferos" | "mamiferos":
            return "MM", "Mamífero"
        case "av" | "ave" | "aves" | "pássaro" | "passaro":
            return "AV", "Ave"
        case "rp" | "réptil" | "reptil" | "répteis" | "repteis":
            return "RP", "Réptil"
        case "ot" | "outro" | "outros":
            return "OT", "Outro"
        case _:
            return None


def _formatar_id(chave: tuple) -> str:
    """Transforma uma chave do dicionário no formato TT-IIIII-AAAA."""
    return f"{chave[0]}-{chave[1]}-{chave[2]}"


def _separar_id_completo(id_pet: str) -> tuple | None:
    """Separa um ID completo, com ou sem hífens, para permitir a busca."""
    if len(id_pet) == 13:
        if id_pet[2] != "-" or id_pet[8] != "-" or id_pet.count("-") != 2:
            return None
        id_sem_hifens = id_pet[:2] + id_pet[3:8] + id_pet[9:]
    elif len(id_pet) == 11 and "-" not in id_pet:
        id_sem_hifens = id_pet
    else:
        return None

    tipo = id_sem_hifens[:2]
    registro = id_sem_hifens[2:7]
    ano = id_sem_hifens[7:]

    if not registro.isdigit() or not ano.isdigit():
        return None

    return tipo, registro, int(ano)


def _buscar_chaves_por_id(cadastro_pets: dict, id_pet: str) -> list:
    """Busca chaves usando o ID completo ou somente o registro sequencial."""
    if not isinstance(id_pet, str):
        return []

    identificador = id_pet.strip().upper()
    id_completo = _separar_id_completo(identificador)

    if id_completo is not None:
        return [id_completo] if id_completo in cadastro_pets else []

    if identificador.isdigit() and 1 <= len(identificador) <= 5:
        registro = identificador.zfill(5)
        return [chave for chave in cadastro_pets if chave[1] == registro]

    return []


def petCreate(
    cadastro_pets: dict,
    tipo_pet: str,
    ano_nascimento: int,
    nome_pet: str,
) -> dict:
    """Cria um pet com ID sequencial e devolve o cadastro atualizado.

    Parâmetros:
        cadastro_pets (dict): dicionário atual de pets cadastrados.
        tipo_pet (str): tipo do pet por extenso ou seu código de duas letras.
        ano_nascimento (int): ano de nascimento do pet.
        nome_pet (str): nome do pet.

    Retorno:
        dict: o próprio dicionário com o novo pet cadastrado.
    """
    if not isinstance(cadastro_pets, dict):
        raise TypeError("O cadastro de pets deve ser um dicionário.")

    tipo_normalizado = _normalizar_tipo(tipo_pet)
    if tipo_normalizado is None:
        raise ValueError("Tipo de pet inválido.")

    if not isinstance(ano_nascimento, int) or not 1000 <= ano_nascimento <= 9999:
        raise ValueError("O ano de nascimento deve ser um número com quatro dígitos.")

    if not isinstance(nome_pet, str) or not nome_pet.strip():
        raise ValueError("O nome do pet não pode ficar vazio.")

    codigo_tipo, tipo_descrito = tipo_normalizado
    registros = []

    for chave in cadastro_pets:
        if isinstance(chave, tuple) and len(chave) >= 2 and str(chave[1]).isdigit():
            registros.append(int(chave[1]))

    proximo_registro = max(registros, default=0) + 1
    if proximo_registro > 99999:
        raise ValueError("Não há mais números de registro disponíveis.")

    registro = f"{proximo_registro:05d}"
    id_pet = f"{codigo_tipo}-{registro}-{ano_nascimento}"
    dados_pet = [nome_pet.strip(), tipo_descrito, ano_nascimento]

    quantidade_anterior = len(cadastro_pets)
    checaCadastroPET(cadastro_pets, id_pet, dados_pet)

    if len(cadastro_pets) == quantidade_anterior:
        raise ValueError("Não foi possível validar o ID criado para o pet.")

    print(f"Cadastro do PET id: {id_pet}, realizado com sucesso!")
    return cadastro_pets


def petRead(cadastro_pets: dict, id_pet: str) -> None:
    """Imprime os pets encontrados por ID, registro ou nome.

    Parâmetros:
        cadastro_pets (dict): dicionário de pets cadastrados.
        id_pet (str): ID completo, registro de cinco dígitos ou nome do pet.

    Retorno:
        None: este procedimento apenas apresenta informações na tela.
    """
    chaves_encontradas = _buscar_chaves_por_id(cadastro_pets, id_pet)

    # O enunciado também testa a busca com "Max". Por isso, se não for um ID,
    # a função procura todos os pets com o nome informado.
    if not chaves_encontradas and isinstance(id_pet, str):
        nome_procurado = id_pet.strip().casefold()
        chaves_encontradas = [
            chave
            for chave, dados in cadastro_pets.items()
            if dados[0].casefold() == nome_procurado
        ]

    if not chaves_encontradas:
        print("O ID do PET não foi encontrado no cadastro.\n")
        print("Confira os dados e tente novamente!")
        return

    for numero, chave in enumerate(chaves_encontradas, start=1):
        nome, tipo, ano = cadastro_pets[chave]
        print("Dados do seu PET:\n")
        print(f"Nome: {nome}")
        print(f"Ano de nascimento: {ano}")
        print(f"Raça: {tipo}")
        print(f"ID: {_formatar_id(chave)}")

        if numero < len(chaves_encontradas):
            print(30 * "-")


def petDelete(cadastro_pets: dict, id_pet: str) -> dict:
    """Remove o pet correspondente ao ID e devolve o cadastro atualizado.

    Parâmetros:
        cadastro_pets (dict): dicionário de pets cadastrados.
        id_pet (str): ID completo ou registro sequencial do pet.

    Retorno:
        dict: o próprio dicionário, com o pet removido quando encontrado.
    """
    chaves_encontradas = _buscar_chaves_por_id(cadastro_pets, id_pet)

    if not chaves_encontradas:
        print("O ID do PET não foi encontrado no cadastro.\n")
        print("Confira os dados e tente novamente!")
        return cadastro_pets

    chave = chaves_encontradas[0]
    id_formatado = _formatar_id(chave)
    del cadastro_pets[chave]
    print(f"Cadastro do PET id: {id_formatado}, removido com sucesso!")
    return cadastro_pets


def petUpdate(cadastro_pets: dict, id_pet: str) -> dict:
    """Solicita novos dados para um pet e devolve o cadastro atualizado.

    Parâmetros:
        cadastro_pets (dict): dicionário de pets cadastrados.
        id_pet (str): ID completo ou registro sequencial do pet.

    Retorno:
        dict: o próprio dicionário, com os dados atualizados quando encontrado.
    """
    chaves_encontradas = _buscar_chaves_por_id(cadastro_pets, id_pet)

    if not chaves_encontradas:
        print("O ID do PET não foi encontrado no cadastro.\n")
        print("Confira os dados e tente novamente!")
        return cadastro_pets

    chave = chaves_encontradas[0]
    dados_pet = cadastro_pets[chave]

    nome_novo = input(f"Novo nome [{dados_pet[0]}]: ").strip()
    tipo_novo = input(f"Novo tipo [{dados_pet[1]}]: ").strip()
    ano_novo = input(f"Novo ano de nascimento [{dados_pet[2]}]: ").strip()

    if nome_novo:
        nome_anterior = dados_pet[0]
        dados_pet[0] = nome_novo
        print(f"O nome '{nome_anterior}' foi substituído por '{nome_novo}'!")

    if tipo_novo:
        tipo_normalizado = _normalizar_tipo(tipo_novo)
        if tipo_normalizado is None:
            print("Tipo inválido. O tipo anterior foi mantido.")
        else:
            tipo_anterior = dados_pet[1]
            dados_pet[1] = tipo_normalizado[1]
            print(
                f"O tipo '{tipo_anterior}' foi substituído por "
                f"'{dados_pet[1]}'!"
            )

    if ano_novo:
        if ano_novo.isdigit():
            ano_anterior = dados_pet[2]
            dados_pet[2] = int(ano_novo)
            print(
                f"O ano '{ano_anterior}' foi substituído por "
                f"'{dados_pet[2]}'!"
            )
        else:
            print("Ano inválido. O ano anterior foi mantido.")

    # A chave não é alterada, pois ela representa o ID original do pet.
    print(f"Cadastro do PET id: {_formatar_id(chave)}, atualizado com sucesso!")
    return cadastro_pets


def petList(cadastro_pets: dict) -> None:
    """Lista, um a um, todos os pets cadastrados.

    Parâmetros:
        cadastro_pets (dict): dicionário de pets cadastrados.

    Retorno:
        None: este procedimento apenas apresenta informações na tela.
    """
    if not cadastro_pets:
        print("Não há pets cadastrados.")
        return

    print("PETS CADASTRADOS")
    print(50 * "-")

    itens_ordenados = sorted(cadastro_pets.items(), key=lambda item: item[0][1])

    for numero, (chave, dados) in enumerate(itens_ordenados, start=1):
        nome, tipo, ano = dados
        print(f"Pet {numero}")
        print(f"Nome: {nome}")
        print(f"Tipo: {tipo}")
        print(f"Ano de nascimento: {ano}")
        print(f"ID: {_formatar_id(chave)}")
        print(50 * "-")


# Em Python, uma função devolve um valor explícito com return para que esse valor
# possa ser usado em outra parte do programa. Um procedimento é o nome dado, por
# convenção, a uma função criada principalmente para executar uma ação, como
# imprimir dados. Python não possui um tipo separado chamado "procedimento": se
# não houver return explícito, a função devolve None automaticamente. Neste módulo,
# petCreate, petDelete e petUpdate são usadas como funções; petRead e petList são
# usadas como procedimentos.


if __name__ == "__main__":
    from unittest.mock import patch

    cadastro_teste = {
        ("CC", "00001", 2024): ["Max", "Cachorro", 2024],
        ("GT", "00002", 2018): ["Miau", "Gato", 2018],
    }

    print("Executando Testes das Funções!!!\n")
    print(50 * "-")

    print("Teste 2-a - petCreate")
    petCreate(cadastro_teste, "OT", 2022, "TESTE")
    print(50 * "-")

    print("Teste 2-b - petRead")
    petRead(cadastro_teste, "Max")
    print(50 * "-")

    print("Teste 2-c - petDelete")
    petDelete(cadastro_teste, "00003")
    print(50 * "-")

    print("Teste 2-d - petUpdate")
    with patch("builtins.input", side_effect=["", "", "2019"]):
        petUpdate(cadastro_teste, "00002")
    print(50 * "-")

    print("Teste 2-e - petList")
    petList(cadastro_teste)
