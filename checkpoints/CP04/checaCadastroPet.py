TIPOS_VALIDOS = ["CC", "GT", "MM", "AV", "RP", "OT"]


def checaCadastroPET(cadastro_pets: dict, id_pet: str, dados_pet: list) -> dict:
    """Valida o ID de um pet e, se ele for válido, adiciona o pet ao cadastro.

    Parâmetros:
        cadastro_pets (dict): dicionário atual de pets cadastrados.
        id_pet (str): ID no formato TT-IIIII-AAAA ou TTIIIIIAAAA.
        dados_pet (list): lista com nome, tipo e ano de nascimento do pet.

    Retorno:
        dict: o próprio dicionário recebido, alterado somente quando o ID é válido.
    """
    if not isinstance(cadastro_pets, dict):
        raise TypeError("O cadastro de pets deve ser um dicionário.")

    if not isinstance(id_pet, str) or not isinstance(dados_pet, list):
        return cadastro_pets

    # Com hífens o ID possui 13 caracteres; sem hífens, possui 11.
    if len(id_pet) == 13:
        if id_pet[2] != "-" or id_pet[8] != "-" or id_pet.count("-") != 2:
            return cadastro_pets
        id_sem_hifens = id_pet[:2] + id_pet[3:8] + id_pet[9:]
    elif len(id_pet) == 11:
        if "-" in id_pet:
            return cadastro_pets
        id_sem_hifens = id_pet
    else:
        return cadastro_pets

    tipo = id_sem_hifens[:2]
    registro = id_sem_hifens[2:7]
    ano_texto = id_sem_hifens[7:]

    if tipo not in TIPOS_VALIDOS:
        return cadastro_pets

    if not registro.isdigit() or int(registro) < 1:
        return cadastro_pets

    # O registro sequencial não pode aparecer em nenhuma outra chave.
    for chave in cadastro_pets:
        if isinstance(chave, tuple) and len(chave) >= 2 and chave[1] == registro:
            return cadastro_pets

    if len(ano_texto) != 4 or not ano_texto.isdigit():
        return cadastro_pets

    cadastro_pets[(tipo, registro, int(ano_texto))] = dados_pet
    return cadastro_pets


if __name__ == "__main__":
    db_pets = {
        ("CC", "00001", 2024): ["Max", "Cachorro", 2024],
        ("GT", "00002", 2018): ["Miau", "Gato", 2018],
    }

    print("Teste 1 - registro repetido; o cadastro deve ser recusado:")
    checaCadastroPET(
        db_pets,
        "CC-00001-2023",
        ["Lulu", "Cachorro", 2020],
    )
    print(db_pets)

    print("\nTeste 2 - ID válido; o cadastro deve ser incluído:")
    checaCadastroPET(
        db_pets,
        "AV000032025",
        ["Loro", "Ave", 2025],
    )
    print(db_pets)
