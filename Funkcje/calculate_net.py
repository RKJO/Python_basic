from typing import Union


def calculate_net(gross: Union[int, float], vat: float) -> float:
    ''' test aplikacji

    >>> calculate_net(123, 0.23)
    100.0
    >>> calculate_net(11.9, 0.19)
    10.0
    '''
    return gross / (1 + vat)


print (calculate_net(123, 0.23))