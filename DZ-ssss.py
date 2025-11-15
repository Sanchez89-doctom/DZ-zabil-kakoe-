class Product:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available

    def __str__(self):
        return f"{self.name} — {self.price} грн, {'в наявності' if self.available else 'нема в наявності'}"


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if not product.available:
            print(f"Товар '{product.name}' недоступний")
            return
        self.items.append(product)
        print(f"Додано: {product.name}")

    def remove_product(self, product_name):
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(f"Видалено {product.name}")
                return
        print(f"Товар '{product_name}' не знайдено")

    def total_price(self):
        return sum(p.price for p in self.items)

    def show_cart(self):
        if not self.items:
            print("Кошик порожній")
            return

        print("Ваш кошик")
        for product in self.items:
            print(f"{product.name}: {product.price} грн")
        print(f"Загальна вартість: {self.total_price()} грн")

p1 = Product("Ноутбук", 25000)
p2 = Product("Мишка", 500)
p3 = Product("Клавіатура", 800, available=False)

cart = Cart()

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

cart.show_cart()

cart.show_cart()