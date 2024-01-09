class Item:
    def __init__(self, id, order, price, quantity):
        self.id = id
        self.order = order
        self.type = None
        if price >= 0:
            self.price = price
        else:
            raise ValueError("Price must be greater than or equal to 0.")
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Quantity must be greater than 0.")

class StockOrders: 
    def __init__(self):
        self.items = []
    
    def add_item(self, item, item_type="Add"):
        item.type = item_type
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_conversion_factor(self, item):
        return round(item.price / item.quantity, 2) if item.quantity != 0 else 'N/A'

    def display_summary(self):
        buy_items = [item for item in self.items if item.order == 'buy']
        sell_items = [item for item in self.items if item.order == 'sell']
  
        best_buy_price = min(buy_items, key=self.calculate_conversion_factor, default=None)
        best_sell_price = max(sell_items, key=self.calculate_conversion_factor, default=None)

        print(f"Best Buy Order: ID {best_buy_price.id if best_buy_price else 'N/A'},"
            f" Price {best_buy_price.price if best_buy_price else 'N/A'},"
            f" Quantity {best_buy_price.quantity if best_buy_price else 'N/A'},"
            f" Conversion factor {round(best_buy_price.price / best_buy_price.quantity, 2) if best_buy_price else 'N/A'}")
        print(f"Best Sell Order: ID {best_sell_price.id if best_sell_price else 'N/A'},"
            f" Price {best_sell_price.price if best_sell_price else 'N/A'},"
            f" Quantity {best_sell_price.quantity if best_sell_price else 'N/A'},"
            f" Conversion factor {round(best_sell_price.price / best_sell_price.quantity, 2) if best_buy_price else 'N/A'}")
