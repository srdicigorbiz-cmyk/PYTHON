# Write code here
taxes = {
    "A":0.18,
    "B":0.10,
    "C":0.07
    }


receipts = []
for r in range(4):
    receipts.append(input().split())

receipts = [[int(x[0]), (x[1])] for x in receipts]

vat = 0

for tax, value in taxes.items():
    for receipt in receipts:
        if receipt[1] == tax:
            vat += receipt[0]*value


print(f"Total VAT paid: {int(vat)}")