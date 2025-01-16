class Basket:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        basket = self.session.get('basket')
        if not basket:
            self.session['basket'] = {}
            self.basket = self.session['basket']
        else:
            self.basket = basket

    
    def addition_product(self, product):
        id = str(product.id)
        if id not in self.basket.keys():
            self.basket[id] = {
                "product_id": product.id,
                "name": product.name,
                "accumulated": int(product.sale_price),
                "quantity": 1,
            }
        else:
            self.basket[id]["quantity"] += 1
            self.basket[id]["accumulated"] += int(product.sale_price)
        self.save_basket()


    def save_basket(self):
        self.session["basket"] = self.basket
        self.session.modified = True


    def delete_product(self, product):
        id = str(product.id)
        if id in self.basket:
            del self.basket[id]
            self.save_basket()


    def subtract_product(self, product):
        id = str(product.id)
        if id in self.basket.keys():
            self.basket[id]["quantity"] -= 1
            self.basket[id]["accumulated"] -= int(product.sale_price)
            if self.basket[id]["quantity"] <= 0:
                self.delete_product(product)
            self.save_basket()


    def wipe_basket(self):
        self.session['basket'] = {}
        self.session.modified = True
