class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_list(self):
        print(f'商品名:{self.name},価格:¥{self.price}')

    def discount(self, discount_amount):
        self.price -= discount_amount

if __name__ == '__main__':
    p1 = Product('アタリメ', 98)
    p1.price_list()
    p1.discount(10)
    p1.price_list()

    p2 = Product('豆乳', 120)
    p2.price_list()
