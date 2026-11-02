class Product:
    current_id = 0
    def __init__(self, description, id_num, price): 
        self.description = description
        self.id_num = Product.current_id
        Product.current_id += 1
        self.price = price

    def __str__(self):
        return f'pruduct {self.description}, id {self.id_num} @{self.price}'
    
ps = [Product('Thinkpad', 0, 1299.95), Product('Mac', 1, 3299.35)] #__init__() is called behind the scenes

for p in ps:
    print(p)

