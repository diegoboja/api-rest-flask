from flask import Flask, jsonify, request

app = Flask(__name__) ## Creo mi aplicacion

from products import products

@app.route('/ping', methods=['GET'])  ## Ruta de prueba de respuesta del servidor
def ping():
    return jsonify({"message":"ping-PONG!"})

@app.route('/products')
def get_products():
    return jsonify(products)

@app.route('/products/<product_name>')
def get_product(product_name):
    product_found = [product for product in products if product['name'] == product_name]
    if len(product_found) > 0 :
        return jsonify(product_found[0])
    return jsonify({"message":"product unavailable"})

@app.route('/products', methods = ['POST'])
def addProduct():
    new_product = {
        'name' : request.json['name'],
        'price': request.json['price'],
        'quantity': request.json['quantity']
    }
    products.append(new_product)
    return jsonify({'message': "Product added", 'products':products})

@app.route('/products/<product_name>', methods = ['PUT'])
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
if __name__ == "__main__":  ## Inicio mi aplicacion y defino el puerto para el servidor
    app.run(debug=True, port=2315)