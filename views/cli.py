def print_contacts(contacts):
    """Exibe contatos formatados em tabela ordenada."""
    if not contacts:
        print("Nenhum contato encontrado.")
        return

    contacts = sorted(contacts, key=lambda c: c.name.lower())
    print(f"{'Nome':<30} | {'Telefone'}")
    print("-" * 45)
    for c in contacts:
        print(f"{c.name:<30} | {c.phone}")