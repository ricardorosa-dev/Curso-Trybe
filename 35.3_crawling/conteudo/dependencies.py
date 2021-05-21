"""Extrai uma lista de dependências de um projeto python"""


def get_dependencies():
    """Le o arquivo requirements.txt e retorna a lista de dependencias"""
    with open("requirements.txt") as reqtxt:
        return [line.split("==")[0] for line in reqtxt]


def get_dependencies_urls(pacotes):
    """Gera urls pros pacotes na lista"""
    return [f"https://pypi.org/project/{pacote}/" for pacote in pacotes]


assert get_dependencies() == ["certifi", "chardet", "idna", "requests", "urllib3"]
