from inventory_report.inventory.product import Product


def test_cria_produto():
    mock_id = 1
    mock_nome_do_produto = "Nome Do Produto"
    mock_nome_da_empresa = "Nome Da Empresa"
    mock_data = "10/10/1010"
    mock_numero_de_serie = "10101010"
    mock_instrucoes_de_armazenamento = "Instruções"

    product = Product(
        mock_id,
        mock_nome_do_produto,
        mock_nome_da_empresa,
        mock_data,
        mock_data,
        mock_numero_de_serie,
        mock_instrucoes_de_armazenamento,
    )

    assert product.id == mock_id
    assert product.nome_do_produto == mock_nome_do_produto
    assert product.nome_da_empresa == mock_nome_da_empresa
    assert product.data_de_fabricacao == mock_data
    assert product.data_de_validade == mock_data
    assert product.numero_de_serie == mock_numero_de_serie
    assert (
        product.instrucoes_de_armazenamento == mock_instrucoes_de_armazenamento
    )
