
from flask import Flask, request, render_template
import json
from http import HTTPStatus
from config import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # warning this disables CORS policy

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
   

@app.get("/about-me")
def about_me():
    user_name = "Tom"
    return render_template("about-me.html", name=user_name)

products = []

#get all products

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.get("/api/products")
def get_products():
    products_db =[]
    cursor = db.products.find({})
    for product in cursor:
        products_db.append(fix_id(product))
    return json.dumps(products_db)

#Post a product
@app.post("/api/products")
def save_products():
    product = request.get_json()
    print(product)
    db.products.insert_one(product)
    return json.dumps(fix_id(product))


############################################
##############coupon codes##################
############################################

@app.get("/api/coupons")
def get_coupons():
    coupons_db =[]
    cursor = db.coupons.find({})
    for coupons in cursor:
        coupons_db.append(fix_id(coupons))
    return json.dumps(coupons_db)

#Post a coupon
@app.post("/api/coupons")
def save_coupons():
    coupons = request.get_json()
    print(coupons)
    db.coupons.insert_one(coupons)
    return json.dumps(fix_id(coupons))







#Put a product
@app.put("/api/products/<int:index>")
def update_products(index):
    update_products = request.get_json()
    print(f"update the product with index {index}")
   
    if 0 <=index < len(products):
        products[index] = update_products
        return json.dumps(update_products), 200
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