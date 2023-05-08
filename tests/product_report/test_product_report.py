from inventory_report.inventory.product import Product
from faker import Faker

fake = Faker("pt-BR")


def test_relatorio_produto():
    id = fake.random_number(digits=1)
    nome_do_produto = fake.word()
    nome_da_empresa = fake.company()
    data = fake.date()
    numero_de_serie = fake.random_number(digits=8)
    instrucoes_de_armazenamento = fake.sentence()

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data,
        data,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    actual = str(product)
    expected = (
        f"O produto {nome_do_produto}"
        f" fabricado em {data}"
        f" por {nome_da_empresa} com validade"
        f" até {data}"
        f" precisa ser armazenado {instrucoes_de_armazenamento}."
    )

    assert actual == expected
