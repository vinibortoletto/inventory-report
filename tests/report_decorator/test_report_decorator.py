from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
import pytest

BLUE = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


@pytest.fixture
def product_list():
    return [
        {
            "id": 1,
            "nome_do_produto": "Cafe",
            "nome_da_empresa": "Cafes Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-08-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "instrucao",
        }
    ]


def test_decorar_relatorio(product_list):
    simple_colored_report = ColoredReport(SimpleReport).generate(product_list)

    assert (
        f"{GREEN}Data de fabricação mais antiga:{RESET} "
        f"{BLUE}2020-07-04{RESET}\n" in simple_colored_report
    )

    assert (
        f"{GREEN}Data de validade mais próxima:{RESET} "
        f"{BLUE}2023-08-09{RESET}\n" in simple_colored_report
    )

    assert (
        f"{GREEN}Empresa com mais produtos:{RESET} "
        f"{RED}Cafes Nature{RESET}" in simple_colored_report
    )
