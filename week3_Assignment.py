def calculate_discount (price, discount_percent) :
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract the discount from the original price
        final_price = price - discount_amount
        return final_price
    else :
        # Return the original price if the discount is less than 20%
        return price
    
    
# Example 1: Discount is 25%
price1 = calculate_discount(450, 25)
print(f"Final price after discount: {price1}")   

# Example 2: Discount is 15%
price2 = calculate_discount(300, 15)
print(f"Final price after discount: {price2}")

# Prompt the user for the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount price:"))

# Calculate the final price 
final_price = calculate_discount(original_price, discount_percentage)

# Print the results
if discount_percentage >=20:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {original_price}")
