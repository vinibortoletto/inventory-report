from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def get_company_product_qty_dict(product_list):
        company_dict = dict()

        for product in product_list:
            company_name = product["nome_da_empresa"]

            if company_name not in company_dict:
                company_dict[company_name] = 1
            else:
                company_dict[company_name] += 1

        return company_dict

    @classmethod
    def generate(self, product_list):
        simple_report = SimpleReport.generate(product_list)
        complete_report = simple_report
        complete_report += "\nProdutos estocados por empresa:\n"
        company_dict = self.get_company_product_qty_dict(product_list)

        for company, qty in company_dict.items():
            complete_report += f"- {company}: {qty}\n"

        return complete_report
