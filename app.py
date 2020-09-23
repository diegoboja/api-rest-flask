from flask import Flask, jsonify, request

app = Flask(__name__) ## Create app

from products import products

@app.route('/', methods=['GET'])  ## Test server 
def ping():
    return jsonify({"message":"Server running OK"})

@app.route('/products') ## Get all products 
def get_products():
    return jsonify(products)

@app.route('/products/<product_name>') ## Get product info
def get_product(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if len(productFound) > 0 :
        return jsonify(productFound[0])
    return jsonify({"message":"product unavailable"})

@app.route('/products', methods = ['POST']) ## Add new product
def addProduct():
    new_product = {
        'name' : request.json['name'],
        'price': request.json['price'],
        'quantity': request.json['quantity']
    }
    products.append(new_product)
    return jsonify({'message': "Product added", 'products':products})

@app.route('/products/<product_name>', methods = ['PUT'])  ## Edit product info
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0) :
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product updated',
            'product updated':productFound[0]
        })
    return jsonify({"message":"product unavailable"})


@app.route('/products/<product_name>', methods = ['DETELE'])  ## Delete product
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        products.remove(productFound[0])
        return jsonify({
            'message': 'Product deleted',
            'products': products
        })
    return jsonify({"message":"product unavailable"})

if __name__ == "__main__":  ## Starting app and setting port
    app.run(debug=True, port=5000)