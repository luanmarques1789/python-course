# CALCULATING DISCOUNT
# --------------------
# Make an algorithm that reads the product price and shows its new price,
# with 5% off.

productPrice = float(input('Enter with product price: '))

newPrice = productPrice * 0.95
print(f'New product price is US${newPrice:.2f}')
