# User operations
REGISTER_USER = "INSERT INTO users (username, password) VALUES (%s, %s)"
LOGIN_USER = "SELECT * FROM users WHERE username = %s AND password = %s"

# Product operations
ADD_PRODUCT = "INSERT INTO products (product_name, description, price, seller_id) VALUES (%s, %s, %s, %s)"
VIEW_PRODUCTS = "SELECT product_id, product_name, description, price, stock FROM products"

# Review operations
LEAVE_REVIEW = "INSERT INTO reviews (product_id, reviewer_id, review_text, rating) VALUES (%s, %s, %s, %s)"
