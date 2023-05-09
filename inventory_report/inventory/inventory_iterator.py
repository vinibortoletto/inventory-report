from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, product_list):
        self.product_list = product_list
        self.index = 0

    def __next__(self):
        try:
            product = self.product_list[self.index]
        except IndexError:
            raise StopIteration()
        else:
            self.index += 1
            return product
