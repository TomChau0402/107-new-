
from flask import Flask, request
import json
from http import HTTPStatus

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from flask"
# @app.post("/")
# @app.put("/")
# @app.patch("/")
# @app.delete("/")

@app.get("/test")
def test():
    return "this is another endpoint"

# This is a JSON implementation
@app.get("/api/about")
def about():
    name={"name":"Tom"}
    return json.dumps(name)
   
products = []

#get all products

@app.get("/api/products")
def get_products():
    return json.dumps(products), HTTPStatus.OK

#Post a product
@app.post("/api/products")
def save_product():
    product = request.get_json()
    print(f"product {product}")
    products.append(product)
    return "Product saved", 201

#Put a product
@app.put("/api/products/<int:index>")
def update_product(index):
    update_product = request.get_json()
    print(f"update the product with index {index}")
   
    if 0 <=index < len(products):
        products[index] = update_product
        return json.dumps(update_product), 200
    else:
        return "that index does not exit", 404



# Delete a product
@app.delete("/api/products/<int:index>")
def delete_product(index):
    print(f"delete the product with index {index}")
    if index >=0 and index < len(products):
        deleted_product = products.pop(index)
        return json.dumps(deleted_product)
    else:
        return "That index does not exit", 404



app.run(debug=True)