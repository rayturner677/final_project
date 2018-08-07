import core


def test_price_of_pizza():
    inventory = {'pizza': {'price': 10}}

    result = core.price_with_tax(inventory, 'pizza')

    assert result == 10.7


def test_add_to_stock():
    inventory = {'hardwear': {'stock': 7}}

    result = core.add_to_stock(inventory, 'hardwear')

    assert inventory['hardwear']['stock'] == 8


def test_find_replacement():
    inventory = {'raspberry': {'replacement': 25}}

    result = core.find_replacement(inventory, 'raspberry')

    assert inventory['raspberry']['replacement'] == 25
    assert result == 2.5
