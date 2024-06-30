import requests

BASE_URL = "http://localhost:8000"

def get_products():
    response = requests.get(f"{BASE_URL}/products/")
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_product_by_id(product_id):
    response = requests.get(f"{BASE_URL}/products/{product_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def chatbot_response(user_input):
    if "list products" in user_input.lower():
        products = get_products()
        if products:
            response = "Here are some products:\n"
            for product in products:
                response += f"{product['name']} - ${product['price']}\n"
            return response
        else:
            return "No products found."
    
    if "product" in user_input.lower():
        product_id = int(user_input.split()[-1])  # Simple extraction of product ID
        product = get_product_by_id(product_id)
        if product:
            return f"Product details:\nName: {product['name']}\nPrice: ${product['price']}\nSize: {product['size']}\nUnits: {product['units']}\nDiscount: {product['discount']}"
        else:
            return "Product not found."

    return "Sorry, I didn't understand that. Please ask about products."