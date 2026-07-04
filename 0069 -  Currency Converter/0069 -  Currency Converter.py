CURRENCIES = {
    'USD': 1,
    'EUR': 1.06,
    'YEN': 0.0067,
    'GBP': 1.23,
    'AUD': 0.64,
    'CAD': 0.74
}

# Write code here
def to_usd(code, amount):
    if code not in CURRENCIES:
        raise Exception(f"{code} is not supported")
    elif amount < 0:
        raise Exception("Invalid amount")
    else:
        return CURRENCIES[code]*amount

def from_usd(code, amount):
    if code not in CURRENCIES:
        raise Exception(f"{code} is not supported")
    elif amount < 0:
        raise Exception("Invalid amount")
    else:
        return round((amount/CURRENCIES[code]),4)

def convert(code_from, amount, code_to):
    try:
        result1 = to_usd(code_from, amount)
        result2 = from_usd(code_to, result1)
        return f"{float(amount)} {code_from} is {result2} {code_to}"
    except Exception as e:
	    print(e)

print(convert("YEN",1000,"GBP"))
print(convert("YEN",1202343,"USD"))
print(convert("EUR",543.12,"GBP"))