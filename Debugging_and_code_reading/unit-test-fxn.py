import pytest 
from pricing import final_price

'''1. Happy path test
Normal valid input:'''

def test_final_price_with_discount():
    result = final_price(1000, 20)

    assert result == 800

'''2. Edge-case test
Boundary values को check करना जरूरी है:'''

@pytest.mark.parametrize(
    "price, discount, expected",
    [
        (1000, 0, 1000),    # minimum discount
        (1000, 100, 0),     # maximum discount
        (0, 20, 0),         # zero price
    ],
)

def test_final_price_edge_cases(price, discount, expected):
    assert final_price(price, discount) == expected   ##running the file == pytest filename.py -v 

'''3. Failure-mode test
Invalid input पर function सही error देता है या नहीं:'''

@pytest.mark.parametrize(
    "price, discount",
    [
        (-100, 10),  ## negative price
        (100, -1),  ## discount below 0
        (100, 101) # discount above 100
     ],
)

def test_final_price_rejects_invalid_values(price, discount):
    with pytest.raises(ValueError):
        final_price(price, discount)