from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def get_product_quantity_by_company(product_list, company_name):
        return len(
            [
                product
                for product in product_list
                if product["nome_da_empresa"] == company_name
            ]
        )

    @classmethod
    def generate(self, product_list):
        simple_report = SimpleReport.generate(product_list)
        complete_report = simple_report
        complete_report += "\nProdutos estocados por empresa:\n"

        for product in product_list:
            company_name = product["nome_da_empresa"]

            quantity = self.get_product_quantity_by_company(
                product_list, company_name
            )

            complete_report += f"- {company_name}: {quantity}\n"

        return complete_report
