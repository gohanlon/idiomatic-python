import decimal

print(decimal.Decimal(355) / decimal.Decimal(113))

with decimal.localcontext(decimal.Context(prec=50)):
    print(decimal.Decimal(355) / decimal.Decimal(113))

print(decimal.Decimal(355) / decimal.Decimal(113))
