from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from tests.factories.product_factory import ProductFactory


BLUE = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


def test_decorar_relatorio():
    product = ProductFactory()
    test = [vars(product)]

    simple_colored_report = ColoredReport(SimpleReport).generate(test)

    assert (
        f"{GREEN}Data de fabricação mais antiga:{RESET} "
        f"{BLUE}{product.data_de_fabricacao}{RESET}\n" in simple_colored_report
    )

    assert (
        f"{GREEN}Data de validade mais próxima:{RESET} "
        f"{BLUE}{product.data_de_validade}{RESET}\n" in simple_colored_report
    )

    assert (
        f"{GREEN}Empresa com mais produtos:{RESET} "
        f"{RED}{product.nome_da_empresa}{RESET}" in simple_colored_report
    )
