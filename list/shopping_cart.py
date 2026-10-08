cart = []

cart.append("Shirt")
cart.append("Shoes")
cart.append("Jeans")

print("Cart:", cart)

cart.remove("Shoes")

if "Shirt" in cart:
    print("Shirt is available")

print("Updated cart:", cart)
print("Total items:", len(cart))