from datetime import datetime


class SimpleReport:
    def get_oldest_manufacturing_date(product_list):
        return min(product["data_de_fabricacao"] for product in product_list)

    def closest_expiration_date(product_list):
        today = datetime.now().strftime("%Y-%m-%d")

        return min(
            product["data_de_validade"]
            for product in product_list
            if product["data_de_validade"] >= today
        )

    def get_company_with_more_products(product_list):
        company_counter = dict()

        for product in product_list:
            company_name = product["nome_da_empresa"]

            if company_name not in company_counter:
                company_counter[company_name] = 1
            else:
                company_counter[company_name] += 1

        return max(company_counter, key=company_counter.get)

    @classmethod
    def generate(self, product_list):
        oldest_manufacturing_date = self.get_oldest_manufacturing_date(
            product_list
        )

        oldest_expiration_date = self.closest_expiration_date(product_list)

        company_with_more_products = self.get_company_with_more_products(
            product_list
        )

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {oldest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
