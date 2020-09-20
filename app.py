from flask import Flask, jsonify

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
    else:
        return jsonify({"message":"product unavailable"})

if __name__ == "__main__":  ## Inicio mi aplicacion y defino el puerto para el servidor
    app.run(debug=True, port=2315)