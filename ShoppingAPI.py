from flask import Flask , jsonify
from itertools import product
from profile import run
from click._compat import raw_input
app = Flask(__name__)

products = [{' name ': "Soap",
              'product_id': "0",
              'Description':"It is India's first brand with this unique combination."
                            "Over 35 years, the brand symbolizes natural ingredients and younger looking skin."
                            "Every Indian household rank Soap high as a skin care essential that helps maintain younger looking skin.16-May-2019",
              'price':"25"},
            {' name ': "Toothpaste",
              'product_id': "1",
              'Description':"It is an American brand principally used for oral hygiene products such as toothpastes, toothbrushes, mouthwashes and dental floss." 
                            "Manufactured by Toothpaste-India, Toothpaste oral hygiene products were first sold by the company in 1873, sixteen years after the death of the founder, William Toothpaste.",
              'price':"95"},
            {' name ': "Salt",
              'product_id': "2",
              'Description':"Salt, in chemistry, substance produced by the reaction of an acid with a base." 
                            "A salt consists of the positive ion (cation) of a base and the negative ion (anion) of an acid. ... The term salt is also used to refer specifically to common table salt, or sodium chloride.",   
              'price':"15"},
            {' name ': "Suger",
              'product_id': "3",
              'Description':"Sugar, any of numerous sweet, colourless, water-soluble compounds present in the sap of seed plants and the milk of mammals and making up the simplest group of carbohydrates."
                            "The most common sugar is sucrose, a crystalline tabletop and industrial sweetener used in foods and beverages.", 
              'price':"45"},
            {' name ': "Oil",
              'product_id':"4",
              'Description':" An oil has been refined by using chemicals that are harmful to us." 
                            "In short it means to 'purify' It may mean the oil was treated with acid, or purified with an alkali, or bleached." 
                            "It can also be neutralized, filtered or deodorized.", 
              'price':"110"},
            {' name ': "Spices",
              'product_id': "5",
              'Description':"A spice is a seed, fruit, root, bark, or other plant substance primarily used for flavoring or coloring food. "
		                    "Spices are distinguished from herbs, which are the leaves, flowers, or stems of plants used for flavoring or as a garnish.",  
              'price':"50"}
            ]


@app.route('/')
def index():
    return "Welcome To the API Of Shopping Cart "

@app.route("/products", methods=['GET'])
def get():
    return jsonify({'Products':products})


@app.route("/products/<int:product_id>",methods=['GET'])
def get_products(product_id):
    return jsonify({'Products':products[product_id]})

@app.route("/products", methods=['POST'])
def create():  
    product =[{'name': "Nuts",
              'product_id': "6",
              'Description':"A nut is a fruit composed of an inedible hard shell and a seed, which is generally edible."
              "In general usage and in a culinary sense, a wide variety of dried seeds are called nuts."
              "but in a botanical context nut implies that the shell does not open to release the seed.",  
              'price':"50"}]

    products.append(product)
    return jsonify({'create':products})

@app.route("/products/<int:product_id>",methods=['PUT'])
def product_update(product_id):
      products[product_id]['Description'] = "XYZ"
      return jsonify({'produt':products[product_id]})
    
@app.route("/products/<int:product_id>",methods=['DELETE'])
def delete(product_id):
      products.remove(products[product_id])
      return jsonify({'result':True})   
    


if __name__ == "__main__":
    app.run(debug=True)