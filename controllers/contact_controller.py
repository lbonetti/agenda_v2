import json
import os
from models.contact import Contact

class ContactController:
    """Gerencia os contatos da agenda."""

    def __init__(self, filepath='contacts.json'):
        self.filepath = filepath
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Carrega contatos do arquivo JSON."""
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, 'r', encoding="utf-8") as f:
            try:
                data = json.load(f)
                return [Contact.from_dict(c) for c in data]
            except json.JSONDecodeError:
                return []

    def save_contacts(self):
        """Salva contatos no arquivo JSON."""
        with open(self.filepath, 'w', encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=2, ensure_ascii=False)

    def add_contact(self, name, phone):
        """Adiciona um novo contato."""
        if not name or not phone:
            raise ValueError("Nome e telefone são obrigatórios.")
        self.contacts.append(Contact(name, phone))
        self.save_contacts()

    def list_contacts(self):
        """Retorna todos os contatos."""
        return self.contacts

    def find_contacts(self, name):
        """Busca parcial e insensível por nome."""
        name = name.lower()
        return [c for c in self.contacts if name in c.name.lower()]

    def delete_contact_interactive(self, name):
        """Exclui contato após seleção interativa."""
        matches = self.find_contacts(name)
        if not matches:
            raise ValueError("Nenhum contato correspondente encontrado.")

        print("Contatos encontrados:")
        for idx, c in enumerate(matches, 1):
            print(f"{idx}. {c.name} - {c.phone}")

        selected = input("Digite o número do contato que deseja excluir (0 para cancelar): ")
        if not selected.isdigit() or not (0 <= int(selected) <= len(matches)):
            raise ValueError("Opção inválida.")

        if int(selected) == 0:
            print("Operação cancelada.")
            return

        contato = matches[int(selected) - 1]
        self.contacts.remove(contato)
        self.save_contacts()
        print("Contato excluído com sucesso.")

    def update_contact_interactive(self, name):
        """Atualiza nome e telefone de um contato selecionado."""
        matches = self.find_contacts(name)
        if not matches:
            raise ValueError("Nenhum contato correspondente encontrado.")

        print("Contatos encontrados:")
        for idx, c in enumerate(matches, 1):
            print(f"{idx}. {c.name} - {c.phone}")

        selected = input("Digite o número do contato que deseja editar (0 para cancelar): ")
        if not selected.isdigit() or not (0 <= int(selected) <= len(matches)):
            raise ValueError("Opção inválida.")

        if int(selected) == 0:
            print("Operação cancelada.")
            return

        contato = matches[int(selected) - 1]

        new_name = input(f"Novo nome (pressione Enter para manter '{contato.name}'): ").strip()
        new_phone = input(f"Novo telefone (pressione Enter para manter '{contato.phone}'): ").strip()

        if new_name:
            contato.name = new_name
        if new_phone:
            contato.phone = new_phone

        self.save_contacts()
        print("Contato atualizado com sucesso.")