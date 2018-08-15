import core


def test_price_of_pizza():
    cost = 70

    result = core.get_tax(cost)

    assert result == 4.9


def test_add_to_stock():
    inventory = {'hardwear': {'stock': 7}}

    result = core.return_item(inventory, 'hardwear')

    assert inventory['hardwear']['stock'] == 8


def test_find_replacement():
    inventory = {'raspberry': {'replacement': 25}}

    result = core.get_deposit(inventory, 'raspberry')

    assert result == 2.5


def test_in_stock_true():
    inventory = {'raspberry': {'stock': 25}}

    result = core.in_stock(inventory, 'raspberry')

    assert result is True


def test_in_stock_false():
    inventory = {'hardwear': {'stock': 0}}

    result = core.in_stock(inventory, 'hardwear')

    assert result is False


def test_rent_item():
    inventory = {'brickcity': {'stock': 5}}

    result = core.rent_item(inventory, 'brickcity')

    assert inventory['brickcity']['stock'] == 4
