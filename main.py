#Lucas Bonetti  06/2025
#Registrar em arquivo local nome e número de telefone
#- Funcionalidades: inserir, excluir, alterar, "olhar"
#- "Olhar": lista tabular de contatos em ordem alfabética com nome e telefone
#- Busca de contatos por nome insensível

import argparse
from controllers.contact_controller import ContactController
from views.cli import print_contacts

def main():
    parser = argparse.ArgumentParser(
        description="Agenda Telefônica",
        epilog="Exemplos:\n"
               "  python3 main.py add --name 'Maria' --phone 11999999999\n"
               "  python3 main.py search --name 'Mar'\n"
               "  python3 main.py update --name 'Mar'\n"
               "  python3 main.py delete --name 'Mar'\n"
               "  python3 main.py list",
        formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command", help="Comando disponível")

    add_parser = subparsers.add_parser("add", help="Adicionar novo contato")
    add_parser.add_argument("--name", required=True, help="Nome do contato")
    add_parser.add_argument("--phone", required=True, help="Telefone do contato")

    search_parser = subparsers.add_parser("search", help="Buscar contatos por nome")
    search_parser.add_argument("--name", required=True, help="Parte do nome para buscar")

    update_parser = subparsers.add_parser("update", help="Editar contato")
    update_parser.add_argument("--name", required=True, help="Parte do nome do contato")

    delete_parser = subparsers.add_parser("delete", help="Excluir contato")
    delete_parser.add_argument("--name", required=True, help="Parte do nome do contato")

    subparsers.add_parser("list", help="Listar todos os contatos")

    args = parser.parse_args()
    controller = ContactController()

    if args.command is None:
        parser.print_help()
        return

    try:
        if args.command == "add":
            controller.add_contact(args.name, args.phone)
            print("Contato adicionado com sucesso.")
        elif args.command == "search":
            contatos = controller.find_contacts(args.name)
            print_contacts(contatos)
        elif args.command == "list":
            contatos = controller.list_contacts()
            print_contacts(contatos)
        elif args.command == "delete":
            controller.delete_contact_interactive(args.name)
        elif args.command == "update":
            controller.update_contact_interactive(args.name)
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()