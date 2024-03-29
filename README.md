# Stock Exchange System

The Stock Exchange System is a Python application for managing stock orders. It includes classes for handling items and stock orders, as well as methods for adding, removing, and displaying order information.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Classes](#classes)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/PiotrZamojski/StockExchange.git
    cd StockExchange
    ```

## Usage

1. Run the main application:

    ```bash
    python3 .\item_orders.py    
    ```

## Classes

### `Item`

The `Item` class represents a stock item with an ID, order type (buy/sell), price, and quantity.

- **Attributes:**
  - `id`: The unique identifier for the item.
  - `order`: The type of order (buy/sell).
  - `type`: The order type (default is `None`).
  - `price`: The price of the item (must be greater than or equal to 0).
  - `quantity`: The quantity of the item (must be greater than 0).

#### Example:

```python
item = Item(id="001", order="buy", price=20.0, quantity=100)
```

### `StockOrders`  

The `StockOrders` class manages a collection of stock items. It provides methods for adding, removing, and displaying order information.

- **Methods**:
  - `add_item(item, item_type="Add")`: Adds an item to the stock with an optional order type.
  - `remove_item(item)`: Removes an item from the stock.
  - `calculate_conversion_factor(item)`: Calculates the conversion factor for an item.
  - `display_summary()`: Displays the best buy and sell orders with their details.

#### Example:
```python
stock_orders = StockOrders()
stock_orders.add_item(item)
stock_orders.add_item(item2)
stock_orders.remove_item(item2)
stock_orders.display_summary()
```
## Features:

Best Conversion Price and Quantity: The application calculates the best conversion price and quantity for both buy and sell orders.