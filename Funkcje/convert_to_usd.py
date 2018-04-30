def convert_to_usd(zlotys):
    return zlotys / 3.85


# poniższe linijki przetestują Twoją funkcję:
print("385PLN = ", convert_to_usd(385), "USD")
print("100PLN = ", convert_to_usd(100), "USD")
print("100PLN =  %.2f" % convert_to_usd(100), "USD")