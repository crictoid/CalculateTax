# Mark Bulmer - CIS 115 - 6-9-2021
# Calculate tax.

subtotal=float(input("Subtotal: $"))
state_tax=subtotal*.05
county_tax=subtotal*.025
total_tax=(state_tax+county_tax)
grand_total=(subtotal+total_tax)
print("Subtotal: $", subtotal)
print("State Tax: $", state_tax)
print("County Tax: $", county_tax)
print("Total Tax: $", total_tax)
print("Grand Total: $", grand_total)
