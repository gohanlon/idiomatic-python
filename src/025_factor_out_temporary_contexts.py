import decimal

print(decimal.Decimal(355) / decimal.Decimal(113))

old_context = decimal.getcontext().copy()
decimal.getcontext().prec = 50
print(decimal.Decimal(355) / decimal.Decimal(113))
decimal.setcontext(old_context)

print(decimal.Decimal(355) / decimal.Decimal(113))
