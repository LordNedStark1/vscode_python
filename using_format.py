import decimal
value = 20.893
# print (f"{value:.4f}")
# print ("{:.2f}".format(value))

float_value_one = f"{value:.2f}"
print (float_value_one)

print( "{:0<9}".format(value))
print(f"{value:A<9}")


decimal.Decimal