class Contact:
    """Classe que representa um contato com nome e telefone."""

    def __init__(self, name: str, phone: str):
        """Inicializa um novo contato."""
        self.name = name.strip()
        self.phone = phone.strip()

    def to_dict(self):
        """Converte o contato para dicionário."""
        return {"name": self.name, "phone": self.phone}

    @staticmethod
    def from_dict(data):
        """Cria um contato a partir de um dicionário."""
        return Contact(data["name"], data["phone"])