class Item:
    def __init__(self, item_id, item_name, description, unit_price, quantity_in_stock, category):
        self.item_id = item_id
        self.item_name = item_name
        self.description = description
        self.unit_price = unit_price
        self.quantity_in_stock = quantity_in_stock
        self.category = category

    @classmethod
    def from_dict(cls, item_data):
        return cls(
            item_id=item_data['item_id'],
            item_name=item_data['item_name'],
            description=item_data['description'],
            unit_price=item_data['unit_price'],
            quantity_in_stock=item_data['quantity_in_stock'],
            category=item_data['category']
        )