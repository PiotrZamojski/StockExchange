import unittest

from item_orders import Item, StockOrders
from unittest.mock import patch
from io import StringIO

class TestStockOrders(unittest.TestCase):
    def setUp(self):
        self.stock_orders = StockOrders()
        self.buy_item_1 = Item("001", "buy", 18.0, 100)
        self.buy_item_2 = Item("002", "buy", 23.0, 50)
        self.sell_item_1 = Item("003", "sell", 30.0, 75)

    def test_add_item(self):
        self.stock_orders.add_item(self.buy_item_1)
        self.assertEqual(len(self.stock_orders.items), 1)

    def test_remove_item(self):
        self.stock_orders.add_item(self.buy_item_1)
        self.stock_orders.add_item(self.buy_item_2)
        self.stock_orders.add_item(self.sell_item_1)
        self.stock_orders.remove_item(self.buy_item_1)
        self.assertEqual(len(self.stock_orders.items), 2)
        self.assertNotIn(self.buy_item_1, self.stock_orders.items)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_summary(self, mock_stdout):
        self.stock_orders.add_item(self.buy_item_1)
        self.stock_orders.add_item(self.buy_item_2)
        self.stock_orders.add_item(self.sell_item_1)

        self.stock_orders.display_summary()
        expected_output = (
            "Best Buy Order: ID 001, Price 18.0, Quantity 100, Conversion factor 0.18\n"
            "Best Sell Order: ID 003, Price 30.0, Quantity 75, Conversion factor 0.4\n"
        )

        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()


