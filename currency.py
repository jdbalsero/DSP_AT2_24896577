
def round_rate(rate):
    """
    Function that will round an input float to 4 decimals places.

    Parameters
    ----------
    rate: float
        Rate to be rounded

    Returns
    -------
    float
        Rounded rate
    """
    return round(rate, ndigits=4)
    

def reverse_rate(rate):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    if rate != 0:
        return round_rate(1/rate)
    else:
        return 0
    
def format_output(date, from_currency, to_currency, rate, amount):
    """
    Function that will use the information about currency pair, amount and the conversion rate
    to produce an output message formatted to follow the template required.

    Parameters
    ----------
    date: str
        Date of the conversion rate applied
    from_currency: str
        Code for the origin currency
    to_currency: str
        Code for the destination currency
    rate: float
        FX conversion rate
    amount: float
        The amount (in origin currency) to be converted
    
    Returns
    -------
    str
        Output message formatted to contain the required data into the template string provided
    """
    return f'The conversion rate on {date} from {from_currency} to {to_currency} was {rate} So {amount} in {from_currency} correspond to {round(amount*rate, 2)} in {to_currency}. The inverse rate was {reverse_rate(rate)}.'
   